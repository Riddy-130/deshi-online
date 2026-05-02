$env:DJANGO_SETTINGS_MODULE = "config.settings.dev"
& ".\venv\Scripts\python.exe" manage.py migrate
& ".\venv\Scripts\python.exe" manage.py seed_store
& ".\venv\Scripts\python.exe" manage.py runserver
