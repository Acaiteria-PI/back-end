# Autenticação

A API utiliza autenticação **JWT (JSON Web Token)** via `djangorestframework-simplejwt`.

## Tempo de Vida dos Tokens

| Token | Duração |
|---|---|
| Token de Acesso | 60 minutos |
| Token de Renovação | 30 dias |

---

## Obter Tokens

**`POST /token/`**

Corpo da requisição:

```json
{
  "email": "usuario@exemplo.com",
  "password": "suasenha"
}
```

Resposta:

```json
{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}
```

---

## Renovar Token de Acesso

**`POST /token/refresh/`**

Corpo da requisição:

```json
{
  "refresh": "<refresh_token>"
}
```

Resposta:

```json
{
  "access": "<novo_access_token>"
}
```

---

## Usando o Token

Inclua o token de acesso no cabeçalho `Authorization` em todas as requisições protegidas:

```
Authorization: Bearer <access_token>
```

---

## Política de Permissões Padrão

A classe de permissão global padrão é `DjangoModelPermissionsOrAnonReadOnly`, o que significa:

- Requisições `GET` são abertas para usuários anônimos na maioria dos endpoints.
- `POST`, `PUT`, `DELETE` exigem um usuário autenticado com as permissões adequadas no nível do modelo.
- Alguns endpoints (ex.: `DailyRevenue`, `users/me/`) exigem explicitamente `IsAuthenticated`.

---

## Modelo de Usuário Customizado

A autenticação é baseada em e-mail. O campo `username` foi removido. O modelo `User` usa `email` como `USERNAME_FIELD`.

```
email        → único, usado para login
name         → nome de exibição
registration → ID de funcionário único (opcional)
establishment → FK para Establishment (a loja à qual o usuário pertence)
```
