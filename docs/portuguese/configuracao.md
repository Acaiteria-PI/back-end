# Configuração e Deploy

## Requisitos

- Python 3.11+
- pip ou [PDM](https://pdm-project.org/)
- PostgreSQL (para produção)

## Desenvolvimento Local

**1. Instalar dependências**

```bash
pip install -r requirements.txt
```

**2. Configurar variáveis de ambiente**

Copie `.env_exemplo` para `.env` e preencha os valores:

```env
SECRET_KEY='sua-chave-secreta'
DEBUG=True
ALLOWED_HOSTS='*'
DATABASE_URL='sqlite:///db.sqlite3'
MODE=DEVELOPMENT
WEB_CONCURRENCY=4
```

| Variável | Descrição | Padrão |
|---|---|---|
| `SECRET_KEY` | Chave secreta do Django | `django-insecure` |
| `DEBUG` | Ativar modo debug | `True` |
| `ALLOWED_HOSTS` | Lista de hosts permitidos separados por vírgula | `""` |
| `DATABASE_URL` | String de conexão com o banco de dados | `sqlite:///db.sqlite3` |
| `MODE` | `DEVELOPMENT` ou `PRODUCTION` | `DEVELOPMENT` |
| `WEB_CONCURRENCY` | Número de workers do Gunicorn | `4` |

**3. Aplicar migrações**

```bash
python manage.py migrate
```

**4. Criar superusuário**

```bash
python manage.py createsuperuser
```

**5. Rodar o servidor de desenvolvimento**

```bash
python manage.py runserver
```

A API estará disponível em `http://localhost:8000`.

---

## Deploy em Produção

O script `build.sh` cuida de todo o processo de build para produção:

```bash
#!/usr/bin/env bash
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

Rodar o servidor com Gunicorn:

```bash
gunicorn config.wsgi:application
```

Ou com Uvicorn (ASGI):

```bash
uvicorn config.asgi:application --host 0.0.0.0 --port 8000
```

---

## Documentação da API (gerada automaticamente)

Com o servidor rodando, a documentação interativa está disponível em:

| Interface | URL |
|---|---|
| Swagger UI | `/api/swagger/` |
| ReDoc | `/api/redoc/` |
| Schema OpenAPI | `/api/schema/` |

---

## Rodando os Testes

```bash
python manage.py test
```
