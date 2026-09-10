@echo off
setlocal EnableExtensions EnableDelayedExpansion
title OMX Safe Recovery Launcher

rem ============================================================
rem OMX Safe Recovery Launcher - FIXED
rem
rem Fixes:
rem - "ECHO is off." / "ECHO가 설정되어 있지 않습니다." log bug
rem - Console always pauses before closing
rem - Step 2 shows which diagnostic command is running
rem - Diagnostic command failures do NOT abort the launcher
rem - Does NOT run slow npm global diagnostic commands
rem
rem Existing safety behavior preserved:
rem - Never deletes session.json
rem - Dead PID  -> backs up stale session.json
rem - Live PID  -> leaves existing session untouched
rem              and creates a unique OMX_ROOT for the new conversation
rem ============================================================

call :MAIN %*
set "FINAL_RC=%ERRORLEVEL%"

echo.
echo ============================================================
echo Launcher finished with exit code: %FINAL_RC%
echo This window will remain open until you press a key.
echo ============================================================
pause >nul
exit /b %FINAL_RC%


:MAIN

rem ------------------------------------------------------------
rem Optional project directory argument
rem ------------------------------------------------------------
if not "%~1"=="" (
    cd /d "%~1"
    if errorlevel 1 (
        echo [ERROR] Cannot change directory to:
        echo   %~1
        exit /b 1
    )
)

set "PROJECT_DIR=%CD%"
set "STATE_DIR=%PROJECT_DIR%\.omx\state"
set "SESSION_FILE=%STATE_DIR%\session.json"
set "LOG_DIR=%PROJECT_DIR%\.omx\repair-logs"

set "LIVE_SESSION=0"
set "AUTO_ISOLATED=0"
set "INSTANCE_ROOT="
set "IDENTITY_BAD=0"
set "OWNER_BAD=0"

for %%I in ("%PROJECT_DIR%") do set "PROJECT_NAME=%%~nxI"
if not defined PROJECT_NAME set "PROJECT_NAME=project"

rem Ensure .omx and log directory exist.
if not exist "%PROJECT_DIR%\.omx" mkdir "%PROJECT_DIR%\.omx" >nul 2>&1
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%" >nul 2>&1

if not exist "%LOG_DIR%" (
    echo [ERROR] Could not create log directory:
    echo   %LOG_DIR%
    exit /b 2
)

for /f %%T in ('powershell -NoProfile -Command "Get-Date -Format yyyyMMdd-HHmmss" 2^>nul') do set "STAMP=%%T"
if not defined STAMP set "STAMP=%RANDOM%-%RANDOM%"

set "LOG_FILE=%LOG_DIR%\omx-repair-%STAMP%.log"
set "DOCTOR_FILE=%LOG_DIR%\omx-doctor-%STAMP%.txt"

call :log "============================================================"
call :log "OMX SAFE RECOVERY"
call :log "Project : %PROJECT_DIR%"
call :log "Time    : %STAMP%"
call :log "============================================================"

rem ------------------------------------------------------------
rem Step 1 - Session pointer check
rem ------------------------------------------------------------
echo.
echo [1/5] Checking OMX session state...

if not exist "%SESSION_FILE%" (
    call :log "[OK] No session.json found."
    goto :doctor
)

set "SESSION_PID="
set "SESSION_FILE_ENV=%SESSION_FILE%"

for /f "usebackq delims=" %%P in (`powershell -NoProfile -Command ^
  "$p=$env:SESSION_FILE_ENV; try { $j=Get-Content -Raw -LiteralPath $p | ConvertFrom-Json; if($null -ne $j.pid){ [Console]::Write([string]$j.pid) } } catch { exit 2 }" 2^>nul`) do (
    set "SESSION_PID=%%P"
)

if not defined SESSION_PID (
    call :log "[WARN] session.json exists but PID could not be read."
    call :log "[SAFE] File was NOT modified."
    goto :doctor
)

call :log "[INFO] session.json PID = !SESSION_PID!"

powershell -NoProfile -Command ^
  "$p=[int64]'!SESSION_PID!'; if(Get-Process -Id $p -ErrorAction SilentlyContinue){exit 0}else{exit 1}" >nul 2>&1

if not errorlevel 1 (
    set "LIVE_SESSION=1"
    call :log "[LIVE] PID !SESSION_PID! is still alive."
    call :log "[SAFE] session.json will NOT be modified."
    call :log "[INFO] The new conversation will use a separate OMX_ROOT."
    goto :doctor
)

call :log "[STALE] PID !SESSION_PID! is not running."

set "BACKUP_FILE=%STATE_DIR%\session.json.stale-%STAMP%.bak"
move /Y "%SESSION_FILE%" "%BACKUP_FILE%" >nul 2>&1

if errorlevel 1 (
    call :log "[ERROR] Failed to back up stale session.json."
    call :log "[SAFE] OMX launch aborted. Original session.json was not deleted."
    exit /b 3
)

call :log "[RECOVERED] Stale session pointer moved to:"
call :log "            %BACKUP_FILE%"


rem ------------------------------------------------------------
rem Step 2 - Diagnostics
rem ------------------------------------------------------------
:doctor
echo.
echo [2/5] Collecting SAFE runtime information...
call :blanklog
call :log "=== NODE / OMX PATHS ==="

echo   - Checking node path...
where node >> "%LOG_FILE%" 2>&1
if errorlevel 1 (
    call :log "[WARN] node was not found in PATH."
) else (
    node --version >> "%LOG_FILE%" 2>&1
    node -p "process.execPath" >> "%LOG_FILE%" 2>&1
)

echo   - Checking AppData npm node...
if exist "%APPDATA%\npm\node.exe" (
    call :log "[INFO] AppData npm node.exe exists:"
    "%APPDATA%\npm\node.exe" --version >> "%LOG_FILE%" 2>&1
    "%APPDATA%\npm\node.exe" -p "process.execPath" >> "%LOG_FILE%" 2>&1
) else (
    call :log "[INFO] No AppData npm node.exe found."
)

echo   - Checking omx path...
where omx >> "%LOG_FILE%" 2>&1
if errorlevel 1 (
    call :log "[ERROR] omx was not found in PATH."
    call :log "[INFO] OMX cannot be launched until its PATH/install is fixed."
    exit /b 4
)

call :blanklog
call :log "=== NPM GLOBAL ==="

echo   - Checking npm path only...
where npm >> "%LOG_FILE%" 2>&1
if errorlevel 1 (
    call :log "[WARN] npm was not found in PATH."
) else (
    call :log "[OK] npm was found in PATH."
    call :log "[INFO] Slow npm diagnostic commands are skipped."
    call :log "[INFO] Skipped: npm prefix -g / npm root -g / npm ls -g"
)

call :blanklog
call :log "=== BUN ==="

echo   - Checking bun path only...
where bun >> "%LOG_FILE%" 2>&1
if errorlevel 1 (
    call :log "[INFO] Bun was not found in PATH."
) else (
    call :log "[INFO] Bun was found in PATH."
)

call :log "[OK] Runtime information collection finished."


rem ------------------------------------------------------------
rem Step 3 - OMX doctor
rem ------------------------------------------------------------
echo.
echo [3/5] Running omx doctor...

omx doctor > "%DOCTOR_FILE%" 2>&1
set "DOCTOR_RC=!ERRORLEVEL!"

if exist "%DOCTOR_FILE%" (
    type "%DOCTOR_FILE%" >> "%LOG_FILE%"
    echo.
    type "%DOCTOR_FILE%"
) else (
    call :log "[WARN] omx doctor did not create an output file."
)


rem ------------------------------------------------------------
rem Step 4 - Parse diagnostics
rem ------------------------------------------------------------
echo.
echo [4/5] Checking diagnostic results...

if exist "%DOCTOR_FILE%" (
    findstr /I /C:"provider unavailable" /C:"[XX] Process identity" "%DOCTOR_FILE%" >nul 2>&1
    if not errorlevel 1 (
        set "IDENTITY_BAD=1"
        call :blanklog
        call :log "[WARN] Process identity provider is still unavailable."
        call :log "[INFO] The launcher keeps the diagnostic evidence intact."
    ) else (
        call :blanklog
        call :log "[OK] No Process identity provider failure detected by this check."
    )

    findstr /I /C:"Unable to determine whether this global install is owned by npm or Bun" "%DOCTOR_FILE%" >nul 2>&1
    if not errorlevel 1 (
        set "OWNER_BAD=1"
        call :log "[WARN] OMX global install ownership is ambiguous (npm/Bun)."
        call :log "[INFO] This launcher does not reinstall OMX automatically."
    )
)


rem ------------------------------------------------------------
rem Step 5 - Concurrent-session isolation and launch
rem ------------------------------------------------------------
echo.
echo [5/5] Preparing OMX launch...
call :blanklog
call :log "=== OMX LAUNCH ==="

if "!LIVE_SESSION!"=="1" (
    set "INSTANCE_BASE=%USERPROFILE%\.omx\instances"

    if not exist "!INSTANCE_BASE!" (
        mkdir "!INSTANCE_BASE!" >nul 2>&1
        if errorlevel 1 (
            call :log "[ERROR] Failed to create OMX instance directory:"
            call :log "        !INSTANCE_BASE!"
            call :log "[SAFE] Existing live session was NOT modified."
            exit /b 5
        )
    )

    set "INSTANCE_ROOT=!INSTANCE_BASE!\!PROJECT_NAME!-conversation-%STAMP%-%RANDOM%"
    mkdir "!INSTANCE_ROOT!" >nul 2>&1

    if errorlevel 1 (
        call :log "[ERROR] Failed to create unique OMX_ROOT:"
        call :log "        !INSTANCE_ROOT!"
        call :log "[SAFE] Existing live session was NOT modified."
        exit /b 6
    )

    set "OMX_ROOT=!INSTANCE_ROOT!"
    set "AUTO_ISOLATED=1"

    call :log "[ISOLATED] Existing live OMX conversation was detected."
    call :log "[SAFE] Existing session remains untouched."
    call :log "[ISOLATED] New conversation OMX_ROOT:"
    call :log "           !OMX_ROOT!"
)

echo.
echo Project : %PROJECT_DIR%
echo Log     : %LOG_FILE%
if "!AUTO_ISOLATED!"=="1" (
    echo OMX_ROOT: !OMX_ROOT!
    echo Mode    : concurrent conversation isolation
) else (
    echo OMX_ROOT: default
    echo Mode    : normal launch
)
echo.

omx
set "OMX_RC=!ERRORLEVEL!"

call :blanklog
call :log "[EXIT] OMX returned code !OMX_RC!"

echo.
echo ============================================================
echo OMX finished.
echo Log: %LOG_FILE%

if "!AUTO_ISOLATED!"=="1" (
    echo.
    echo NOTE:
    echo A live OMX conversation was already using this checkout.
    echo The original session was left untouched.
    echo This conversation used:
    echo   !OMX_ROOT!
)

if "!IDENTITY_BAD!"=="1" (
    echo.
    echo NOTE:
    echo Process identity provider is still unavailable.
)

if "!OWNER_BAD!"=="1" (
    echo.
    echo NOTE:
    echo OMX still reports ambiguous npm/Bun global-install ownership.
    echo This is separate from session_pointer_owner_conflict.
)

echo ============================================================

exit /b !OMX_RC!


rem ------------------------------------------------------------
rem Logging helpers
rem ------------------------------------------------------------
:blanklog
echo.
>> "%LOG_FILE%" echo.
exit /b 0

:log
if "%~1"=="" (
    call :blanklog
    exit /b 0
)
echo %~1
>> "%LOG_FILE%" echo %~1
exit /b 0
