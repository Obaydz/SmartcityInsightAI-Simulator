@echo off
chcp 65001 >nul
echo =====================================================================
echo  SmartCity Traffic Simulator — Cap Bon Nord-Est (Kélibia / El Haouaria) (Port 8001)
echo =====================================================================
cd /d "%~dp0"

set "PYTHON_CMD="
if exist ".\venv\Scripts\python.exe" (
    call .\venv\Scripts\activate.bat
    set "PYTHON_CMD=.\venv\Scripts\python.exe"
) else if exist ".\.venv\Scripts\python.exe" (
    call .\.venv\Scripts\activate.bat
    set "PYTHON_CMD=.\.venv\Scripts\python.exe"
) else if exist "%LOCALAPPDATA%\Python\bin\python.exe" (
    set "PYTHON_CMD=%LOCALAPPDATA%\Python\bin\python.exe"
) else (
    where py >nul 2>&1
    if not errorlevel 1 (
        set "PYTHON_CMD=py -3"
    ) else (
        set "PYTHON_CMD=python"
    )
)

%PYTHON_CMD% -m uvicorn main:app --host 127.0.0.1 --port 8001 --reload
pause
