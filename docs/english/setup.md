# Setup & Deployment

## Requirements

- Python 3.11+
- pip or [PDM](https://pdm-project.org/)
- PostgreSQL (for production)

## Local Development

**1. Clone and install dependencies**

```bash
pip install -r requirements.txt
```

**2. Configure environment variables**

Copy `.env_exemplo` to `.env` and fill in the values:

```env
SECRET_KEY='your-secret-key'
DEBUG=True
ALLOWED_HOSTS='*'
DATABASE_URL='sqlite:///db.sqlite3'
MODE=DEVELOPMENT
WEB_CONCURRENCY=4
```

| Variable | Description | Default |
|---|---|---|
| `SECRET_KEY` | Django secret key | `django-insecure` |
| `DEBUG` | Enable debug mode | `True` |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts | `""` |
| `DATABASE_URL` | Database connection string | `sqlite:///db.sqlite3` |
| `MODE` | `DEVELOPMENT` or `PRODUCTION` | `DEVELOPMENT` |
| `WEB_CONCURRENCY` | Number of Gunicorn workers | `4` |

**3. Apply migrations**

```bash
python manage.py migrate
```

**4. Create a superuser**

```bash
python manage.py createsuperuser
```

**5. Run the development server**

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000`.

---

## Production Deployment

The `build.sh` script handles the full production build:

```bash
#!/usr/bin/env bash
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

Run the server with Gunicorn:

```bash
gunicorn config.wsgi:application
```

Or with Uvicorn (ASGI):

```bash
uvicorn config.asgi:application --host 0.0.0.0 --port 8000
```

---

## API Documentation (Auto-generated)

Once the server is running, the interactive docs are available at:

| Interface | URL |
|---|---|
| Swagger UI | `/api/swagger/` |
| ReDoc | `/api/redoc/` |
| OpenAPI Schema | `/api/schema/` |

---

## Running Tests

```bash
python manage.py test
```
