@echo off
setlocal EnableExtensions EnableDelayedExpansion

rem ============================================================
rem OMX Session Pointer Diagnostic / Safe Repair for Windows
rem
rem Usage:
rem   omx-session-repair.bat          Diagnose and auto-repair only stale pointers
rem   omx-session-repair.bat check    Diagnose only; never modify files
rem   omx-session-repair.bat help     Show help
rem
rem Safety policy:
rem   - session.json missing is NOT treated as an error.
rem   - session.json is changed only when OMX doctor reports stale/dead state.
rem   - before removal, session.json is copied to a timestamped backup.
rem   - the script never kills processes and never removes other OMX state files.
rem ============================================================

set "MODE=repair"
if /I "%~1"=="check" set "MODE=check"
if /I "%~1"=="help" goto :HELP
if /I "%~1"=="/?" goto :HELP
if not "%~1"=="" if /I not "%~1"=="check" if /I not "%~1"=="help" if /I not "%~1"=="/?" (
    echo [ERROR] Unknown argument: %~1
    echo.
    goto :HELP
)

echo ============================================================
echo OMX Session Pointer Diagnostic / Safe Repair
echo ============================================================
echo Starting directory: %CD%
echo Mode: %MODE%
echo.

rem ------------------------------------------------------------
rem 1. Confirm OMX command exists
rem ------------------------------------------------------------
where omx >nul 2>&1
if errorlevel 1 (
    echo [ERROR] 'omx' was not found in PATH.
    echo         Open the same shell where OMX normally works, then rerun.
    exit /b 10
)

for /f "delims=" %%I in ('where omx 2^>nul') do (
    set "OMX_CMD=%%I"
    goto :FOUND_OMX
)
:FOUND_OMX
echo [OK] OMX command: %OMX_CMD%

rem ------------------------------------------------------------
rem 2. Resolve OMX root
rem    Priority:
rem      A. explicit OMX_ROOT environment variable
rem      B. nearest parent directory containing .omx
rem ------------------------------------------------------------
set "RESOLVED_OMX_ROOT="
set "ROOT_SOURCE="

if defined OMX_ROOT (
    set "RESOLVED_OMX_ROOT=%OMX_ROOT%"
    set "ROOT_SOURCE=OMX_ROOT environment variable"
) else (
    call :FIND_PROJECT_OMX "%CD%"
)

if not defined RESOLVED_OMX_ROOT (
    echo [INFO] No project .omx directory was found from the current directory upward.
    echo [INFO] This is not automatically an error; OMX may still use another state root.
    echo.
    set "SESSION_FILE="
) else (
    set "SESSION_FILE=%RESOLVED_OMX_ROOT%\state\session.json"
    echo [OK] Resolved OMX root: %RESOLVED_OMX_ROOT%
    echo [OK] Root source: %ROOT_SOURCE%
    echo [INFO] Session pointer: %SESSION_FILE%
    echo.
)

rem ------------------------------------------------------------
rem 3. Run OMX doctor and keep exact output for diagnosis
rem ------------------------------------------------------------
set "TMP_DOCTOR=%TEMP%\omx-doctor-%RANDOM%-%RANDOM%.txt"

echo -------------------- omx doctor ---------------------------
omx doctor > "%TMP_DOCTOR%" 2>&1
set "DOCTOR_RC=%ERRORLEVEL%"
type "%TMP_DOCTOR%"
echo -----------------------------------------------------------
echo [INFO] omx doctor exit code: %DOCTOR_RC%
echo.

set "STALE_FOUND=0"
findstr /I /C:"stale-dead" /C:"session_pointer_unusable" /C:"pointer is stale" "%TMP_DOCTOR%" >nul 2>&1
if not errorlevel 1 set "STALE_FOUND=1"

rem ------------------------------------------------------------
rem 4. Missing session.json is a valid state
rem ------------------------------------------------------------
if not defined SESSION_FILE goto :NO_RESOLVED_SESSION

if not exist "%SESSION_FILE%" (
    echo [OK] session.json does not exist at the resolved project state root.
    echo      This is a valid state and is NOT treated as an error.
    echo.

    if "%STALE_FOUND%"=="1" (
        echo [WARN] OMX doctor reports a stale/unusable session pointer, but the
        echo        resolved session.json does not exist.
        echo.
        echo        Likely causes:
        echo        - OMX is using a different state root.
        echo        - OMX_ROOT differs between shells.
        echo        - stale state is stored outside this project-local path.
        echo.
        call :SHOW_ENV_HINTS
        del "%TMP_DOCTOR%" >nul 2>&1
        exit /b 20
    )

    echo [RESULT] Nothing needs repair. You can run 'omx' normally.
    del "%TMP_DOCTOR%" >nul 2>&1
    exit /b 0
)

rem ------------------------------------------------------------
rem 5. Existing session.json: only modify if doctor says stale
rem ------------------------------------------------------------
echo [INFO] session.json exists.

if "%STALE_FOUND%"=="0" (
    echo [OK] OMX doctor did not report a stale/dead session pointer.
    echo [RESULT] No repair was performed.
    del "%TMP_DOCTOR%" >nul 2>&1
    exit /b 0
)

echo [WARN] OMX doctor reports a stale/unusable session pointer.
echo.

if /I "%MODE%"=="check" (
    echo [CHECK MODE] No files will be changed.
    echo [RESULT] Repair is recommended for:
    echo          %SESSION_FILE%
    del "%TMP_DOCTOR%" >nul 2>&1
    exit /b 21
)

rem ------------------------------------------------------------
rem 6. Safe repair: backup, then remove only session.json
rem ------------------------------------------------------------
call :MAKE_TIMESTAMP
set "BACKUP_FILE=%SESSION_FILE%.bak-%STAMP%"

echo [INFO] Backing up stale session pointer...
copy /Y "%SESSION_FILE%" "%BACKUP_FILE%" >nul
if errorlevel 1 (
    echo [ERROR] Could not create backup:
    echo         %BACKUP_FILE%
    echo [RESULT] Nothing was deleted.
    del "%TMP_DOCTOR%" >nul 2>&1
    exit /b 30
)

echo [OK] Backup created:
echo      %BACKUP_FILE%

del /F /Q "%SESSION_FILE%" >nul 2>&1
if exist "%SESSION_FILE%" (
    echo [ERROR] Could not remove stale session.json.
    echo         Check permissions or whether another program has locked it.
    echo [INFO] Backup remains at:
    echo        %BACKUP_FILE%
    del "%TMP_DOCTOR%" >nul 2>&1
    exit /b 31
)

echo [OK] Removed stale session.json only.
echo.

rem ------------------------------------------------------------
rem 7. Verify after repair
rem ------------------------------------------------------------
echo ---------------- post-repair doctor -----------------------
omx doctor > "%TMP_DOCTOR%" 2>&1
set "VERIFY_RC=%ERRORLEVEL%"
type "%TMP_DOCTOR%"
echo -----------------------------------------------------------
echo.

findstr /I /C:"stale-dead" /C:"session_pointer_unusable" /C:"pointer is stale" "%TMP_DOCTOR%" >nul 2>&1
if not errorlevel 1 (
    echo [WARN] Stale/unusable state is still reported after session.json removal.
    echo [INFO] The script intentionally did not delete any additional OMX files.
    echo [INFO] Backup:
    echo        %BACKUP_FILE%
    echo.
    call :SHOW_ENV_HINTS
    del "%TMP_DOCTOR%" >nul 2>&1
    exit /b 40
)

echo [SUCCESS] Stale project session pointer was safely cleared.
echo [INFO] Backup:
echo        %BACKUP_FILE%
echo.
echo Next step:
echo   omx

del "%TMP_DOCTOR%" >nul 2>&1
exit /b 0

:NO_RESOLVED_SESSION
if "%STALE_FOUND%"=="1" (
    echo [WARN] OMX doctor reports stale/unusable session state, but this script
    echo        could not resolve a project-local OMX root.
    echo.
    call :SHOW_ENV_HINTS
    del "%TMP_DOCTOR%" >nul 2>&1
    exit /b 22
)

echo [RESULT] No project-local OMX root/session pointer was found, and doctor
 echo         did not report stale state. Nothing needs repair.
del "%TMP_DOCTOR%" >nul 2>&1
exit /b 0

:FIND_PROJECT_OMX
set "SCAN_DIR=%~1"
:SCAN_LOOP
if exist "%SCAN_DIR%\.omx\" (
    set "RESOLVED_OMX_ROOT=%SCAN_DIR%\.omx"
    set "ROOT_SOURCE=nearest project .omx directory"
    exit /b 0
)
for %%P in ("%SCAN_DIR%\..") do set "PARENT_DIR=%%~fP"
if /I "%PARENT_DIR%"=="%SCAN_DIR%" exit /b 0
set "SCAN_DIR=%PARENT_DIR%"
goto :SCAN_LOOP

:MAKE_TIMESTAMP
for /f %%I in ('powershell -NoProfile -Command "Get-Date -Format yyyyMMdd-HHmmss"') do set "STAMP=%%I"
if not defined STAMP set "STAMP=backup"
exit /b 0

:SHOW_ENV_HINTS
echo ---------------- environment hints -----------------------
if defined OMX_ROOT (
    echo OMX_ROOT=%OMX_ROOT%
) else (
    echo OMX_ROOT is not set in this shell.
)
echo Current directory=%CD%
echo USERPROFILE=%USERPROFILE%
echo.
echo Suggested commands:
echo   echo %%OMX_ROOT%%
echo   omx doctor
echo   where omx
echo -----------------------------------------------------------
exit /b 0

:HELP
echo OMX Session Pointer Diagnostic / Safe Repair
echo.
echo Usage:
echo   %~nx0
 echo       Diagnose and auto-repair session.json only when OMX doctor
 echo       reports stale/dead or unusable session state.
echo.
echo   %~nx0 check
 echo       Diagnose only. Never modifies files.
echo.
echo   %~nx0 help
 echo       Show this help.
echo.
echo Important:
echo   Missing session.json is considered normal, not an error.
echo   The script never kills a process and never deletes other OMX state files.
exit /b 0
