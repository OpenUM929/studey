@echo off
setlocal EnableExtensions DisableDelayedExpansion
title OMX Safe Session Pointer Repair

rem ============================================================
rem OMX Safe Session Pointer Repair for Windows
rem
rem Default:
rem   omx-safe-session-repair.bat
rem
rem Modes:
rem   check  - Diagnose only. Never changes session state.
rem   repair - Diagnose and use OMX official pointer recovery.
rem   local  - Ignore inherited OMX_ROOT for THIS BAT only,
rem            then diagnose/recover the project-local/default root.
rem   run    - Repair first, then launch OMX if healthy.
rem
rem Safety:
rem   - Never kills a PID.
rem   - Never deletes session.json directly.
rem   - Never permanently changes OMX_ROOT.
rem   - Uses "omx session pointer recover" only if supported.
rem ============================================================

set "MODE=repair"
if /I "%~1"=="check"  set "MODE=check"
if /I "%~1"=="repair" set "MODE=repair"
if /I "%~1"=="local"  set "MODE=local"
if /I "%~1"=="run"    set "MODE=run"

echo.
echo ============================================================
echo OMX Safe Session Pointer Repair
echo ============================================================
echo Working directory : %CD%
echo Mode              : %MODE%
echo.

where omx >nul 2>&1
if errorlevel 1 (
    echo [ERROR] "omx" was not found in PATH.
    echo         Install or repair oh-my-codex first.
    echo.
    exit /b 10
)

echo [INFO] OMX executable:
where omx
echo.

echo [INFO] OMX version:
omx --version 2>&1
echo.

if defined OMX_ROOT (
    echo [INFO] OMX_ROOT is currently set:
    echo        %OMX_ROOT%
) else (
    echo [INFO] OMX_ROOT is not set.
)

if /I "%MODE%"=="local" (
    if defined OMX_ROOT (
        echo.
        echo [INFO] LOCAL mode selected.
        echo        OMX_ROOT will be ignored inside THIS BAT process only.
        echo        Your permanent/user environment variable is NOT changed.
        set "OMX_ROOT="
    )
)
echo.

set "DOCTOR_FILE=%TEMP%\omx_doctor_%RANDOM%_%RANDOM%.txt"

echo ------------------------------------------------------------
echo [1/3] Running: omx doctor
echo ------------------------------------------------------------
omx doctor >"%DOCTOR_FILE%" 2>&1
set "DOCTOR_RC=%ERRORLEVEL%"
type "%DOCTOR_FILE%"
echo.

if not "%DOCTOR_RC%"=="0" (
    echo [WARN] "omx doctor" returned exit code %DOCTOR_RC%.
    echo.
)

findstr /I /C:"ptr=stale" /C:"session_pointer_unusable" "%DOCTOR_FILE%" >nul 2>&1
if errorlevel 1 (
    echo ============================================================
    echo [RESULT] No stale session-pointer condition was detected.
    echo ============================================================
    del /q "%DOCTOR_FILE%" >nul 2>&1

    if /I "%MODE%"=="run" (
        echo.
        echo [INFO] Launching OMX...
        echo.
        omx
        exit /b %ERRORLEVEL%
    )

    echo You can run "omx" normally.
    exit /b 0
)

echo ============================================================
echo [WARN] A stale/stale-like session pointer was detected.
echo ============================================================
echo.

if /I "%MODE%"=="check" (
    echo [CHECK ONLY] No recovery command was executed.
    echo.
    del /q "%DOCTOR_FILE%" >nul 2>&1
    exit /b 20
)

echo ------------------------------------------------------------
echo [2/3] Checking official OMX pointer recovery support
echo ------------------------------------------------------------

omx session pointer recover --help >nul 2>&1
if errorlevel 1 (
    echo [ERROR] This OMX installation does not expose:
    echo.
    echo         omx session pointer recover
    echo.
    echo The BAT will NOT delete or rename session.json manually.
    echo Update oh-my-codex, then run this BAT again:
    echo.
    echo         npm install -g oh-my-codex@latest
    echo         omx setup
    echo         omx doctor
    echo.
    del /q "%DOCTOR_FILE%" >nul 2>&1
    exit /b 30
)

echo [OK] Official pointer recovery command is available.
echo.
echo [INFO] Running:
echo        omx session pointer recover --cwd "%CD%" --json
echo.

omx session pointer recover --cwd "%CD%" --json
set "RECOVER_RC=%ERRORLEVEL%"
echo.

if not "%RECOVER_RC%"=="0" (
    echo [WARN] Pointer recovery returned exit code %RECOVER_RC%.
    echo        OMX may have safely refused recovery because ownership
    echo        could not be proven dead/non-reused.
    echo        No manual deletion will be attempted.
    echo.
)

echo ------------------------------------------------------------
echo [3/3] Re-running: omx doctor
echo ------------------------------------------------------------

omx doctor >"%DOCTOR_FILE%" 2>&1
set "FINAL_DOCTOR_RC=%ERRORLEVEL%"
type "%DOCTOR_FILE%"
echo.

findstr /I /C:"ptr=stale" /C:"session_pointer_unusable" "%DOCTOR_FILE%" >nul 2>&1
if errorlevel 1 (
    echo ============================================================
    echo [SUCCESS] The stale session-pointer warning is no longer present.
    echo ============================================================
    del /q "%DOCTOR_FILE%" >nul 2>&1

    if /I "%MODE%"=="run" (
        echo.
        echo [INFO] Launching OMX...
        echo.
        omx
        exit /b %ERRORLEVEL%
    )

    echo.
    echo Next command:
    echo     omx
    exit /b 0
)

echo ============================================================
echo [NOT REPAIRED] OMX still reports a stale session pointer.
echo ============================================================
echo.
echo Safety stop: this BAT will not kill processes or delete
echo session.json directly.
echo.
if defined OMX_ROOT (
    echo Current OMX_ROOT:
    echo     %OMX_ROOT%
    echo.
    echo If this external root was NOT intentional, test the project
    echo without it by running:
    echo.
    echo     %~nx0 local
    echo.
)
echo If OMX_ROOT is intentional, inspect the recovery JSON above.
echo A refused recovery can mean the owner identity is ambiguous,
echo reused, or otherwise unsafe to mutate automatically.
echo.

del /q "%DOCTOR_FILE%" >nul 2>&1
exit /b 40
