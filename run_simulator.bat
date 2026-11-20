@echo off
echo =====================================================================
echo  SmartCity Traffic Simulator — Grand Tunis (FastAPI Port 8001)
echo =====================================================================
cd /d "%~dp0"
if exist ".\venv\Scripts\activate.bat" (
    call .\venv\Scripts\activate.bat
)
python -m uvicorn main:app --host 127.0.0.1 --port 8001 --reload
pause
