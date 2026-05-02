$env:DJANGO_SETTINGS_MODULE = $env:DJANGO_SETTINGS_MODULE
if (-not $env:DJANGO_SETTINGS_MODULE) {
  $env:DJANGO_SETTINGS_MODULE = "config.settings.dev"
}
python manage.py migrate
python manage.py seed_store
python manage.py runserver 0.0.0.0:8000
