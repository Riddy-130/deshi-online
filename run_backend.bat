@echo off
echo Starting Deshi Product Backend...
cd /d "%~dp0backend"
echo.
echo Make sure you have activated your virtual environment if you use one.
echo If not using venv, skip this step.
echo.
echo Starting Django server at http://127.0.0.1:8000
python manage.py runserver 127.0.0.1:8000