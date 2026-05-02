## Frontend to Backend Connection

Default API base URL resolution:

- Web/Desktop: `http://127.0.0.1:8000`
- Android emulator: `http://10.0.2.2:8000`

Override manually:

```bash
flutter run --dart-define=API_BASE_URL=http://127.0.0.1:8000
```

Production build example:

```bash
flutter build web --dart-define=APP_ENV=production --dart-define=API_BASE_URL=https://api.example.com
```

Backend endpoints used by the app:

- `GET /api/v1/storefront/`
- `GET /api/v1/products/`

Architecture:

- `lib/core/config`: environment and build-time config
- `lib/core/network`: shared API client
- `lib/features/store/data`: repository that talks to the backend
