# Overview

**Pé de Açaí** is a REST API built to manage the full operation of an açaí shop — from menu and stock management to order processing and daily revenue tracking.

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Django 6.0.2 |
| API | Django REST Framework 3.16 |
| Authentication | JWT via `djangorestframework-simplejwt` |
| API Docs | `drf-spectacular` (Swagger / ReDoc) |
| Database | PostgreSQL (production), SQLite (development) |
| Server | Gunicorn + Uvicorn |
| Filtering | `django-filter` |
| CORS | `django-cors-headers` |

## Project Structure

```
.
├── config/                  # Django project settings, URLs, WSGI/ASGI
├── core/
│   ├── adress/              # Address model
│   ├── establishment/       # Main domain: menu, stock, revenue
│   ├── orders/              # Order and order item management
│   ├── supplier/            # Supplier and contact management
│   └── users/               # Custom user model and auth
├── staticfiles/             # Collected static files
├── manage.py
├── build.sh                 # Production build script
├── requirements.txt
└── .env_exemplo             # Environment variable template
```

## Allowed Frontend Origins (CORS)

- `http://localhost:5173`
- `http://127.0.0.1:5173`
- `https://pe-de-acai.vercel.app`
- `https://front-end-ztyr.vercel.app`
- `https://pedeacaiapp.netlify.app`
