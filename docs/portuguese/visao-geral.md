# Visão Geral

**Pé de Açaí** é uma API REST construída para gerenciar a operação completa de uma loja de açaí — desde o cardápio e controle de estoque até o processamento de pedidos e acompanhamento do faturamento diário.

## Stack Tecnológica

| Camada | Tecnologia |
|---|---|
| Framework | Django 6.0.2 |
| API | Django REST Framework 3.16 |
| Autenticação | JWT via `djangorestframework-simplejwt` |
| Docs da API | `drf-spectacular` (Swagger / ReDoc) |
| Banco de Dados | PostgreSQL (produção), SQLite (desenvolvimento) |
| Servidor | Gunicorn + Uvicorn |
| Filtragem | `django-filter` |
| CORS | `django-cors-headers` |

## Estrutura do Projeto

```
.
├── config/                  # Configurações do Django, URLs, WSGI/ASGI
├── core/
│   ├── adress/              # Modelo de endereço
│   ├── establishment/       # Domínio principal: cardápio, estoque, faturamento
│   ├── orders/              # Gerenciamento de pedidos e itens de pedido
│   ├── supplier/            # Gerenciamento de fornecedores e contatos
│   └── users/               # Modelo de usuário customizado e autenticação
├── staticfiles/             # Arquivos estáticos coletados
├── manage.py
├── build.sh                 # Script de build para produção
├── requirements.txt
└── .env_exemplo             # Template de variáveis de ambiente
```

## Origens Frontend Permitidas (CORS)

- `http://localhost:5173`
- `http://127.0.0.1:5173`
- `https://pe-de-acai.vercel.app`
- `https://front-end-ztyr.vercel.app`
- `https://pedeacaiapp.netlify.app`
