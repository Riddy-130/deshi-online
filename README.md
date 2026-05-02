# Deshi Product Backend

This backend uses Django REST Framework with SQLite and is structured for both local development and production-style deployment.

## Run

```bash
python manage.py migrate
python manage.py seed_store
python manage.py runserver
```

Windows shortcut scripts:

```powershell
cd backend
.\runserver.ps1
```

```bat
cd backend
runserver.bat
```

Environment variables:

```bash
DJANGO_SETTINGS_MODULE=config.settings.dev
DJANGO_DEBUG=true
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
DJANGO_CORS_ALLOW_ALL=true
```

Production-style run:

```bash
set DJANGO_SETTINGS_MODULE=config.settings.prod
python manage.py collectstatic --noinput
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

Docker run:

```bash
docker compose up --build
```

## API

Primary professional API version:

- `GET /api/v1/health/`
- `GET /api/v1/categories/`
- `GET /api/v1/products/`
- `GET /api/v1/storefront/`

Backward-compatible aliases are also available under `/api/`.

- `GET /api/health/`
- `GET /api/categories/`
- `GET /api/products/`
- `GET /api/storefront/`
- `GET /api/products/?featured=true`
- `GET /api/products/?category=vegetables`
- `GET /api/products/?q=tomato`
