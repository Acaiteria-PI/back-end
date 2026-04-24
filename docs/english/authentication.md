# Authentication

The API uses **JWT (JSON Web Token)** authentication via `djangorestframework-simplejwt`.

## Token Lifetimes

| Token | Lifetime |
|---|---|
| Access Token | 60 minutes |
| Refresh Token | 30 days |

---

## Obtain Tokens

**`POST /token/`**

Request body:

```json
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```

Response:

```json
{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}
```

---

## Refresh Access Token

**`POST /token/refresh/`**

Request body:

```json
{
  "refresh": "<refresh_token>"
}
```

Response:

```json
{
  "access": "<new_access_token>"
}
```

---

## Using the Token

Include the access token in the `Authorization` header for all protected requests:

```
Authorization: Bearer <access_token>
```

---

## Default Permission Policy

The global default permission class is `DjangoModelPermissionsOrAnonReadOnly`, meaning:

- `GET` requests are open to anonymous users on most endpoints.
- `POST`, `PUT`, `DELETE` require an authenticated user with the appropriate model-level permissions.
- Some endpoints (e.g., `DailyRevenue`, `users/me/`) explicitly require `IsAuthenticated`.

---

## Custom User Model

Authentication is email-based. The `username` field is removed. The `User` model uses `email` as the `USERNAME_FIELD`.

```
email       → unique, used for login
name        → display name
registration → optional unique integer ID
establishment → FK to Establishment (the shop the user belongs to)
```
