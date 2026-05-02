@echo off
set DJANGO_SETTINGS_MODULE=config.settings.dev
call .\venv\Scripts\python.exe manage.py migrate
call .\venv\Scripts\python.exe manage.py seed_store
call .\venv\Scripts\python.exe manage.py runserver
