# API Reference

All endpoints are prefixed with `/api/`. Authentication uses JWT — see [authentication.md](./authentication.md).

> Interactive docs available at `/api/swagger/` and `/api/redoc/`.

---

## Establishments

**Base URL:** `/api/establishments/`

| Method | URL | Description | Auth Required |
|---|---|---|---|
| GET | `/api/establishments/` | List all establishments | No |
| POST | `/api/establishments/` | Create an establishment | Yes |
| GET | `/api/establishments/{id}/` | Retrieve an establishment | No |
| PUT | `/api/establishments/{id}/` | Update an establishment | Yes |
| DELETE | `/api/establishments/{id}/` | Delete an establishment | Yes |

**Query params:** `?search=<name>`

**Fields:**

```json
{
  "id": 1,
  "name": "Pé de Açaí Centro",
  "cnpj": "12345678000195",
  "amount": "10000.00"
}
```

---

## Ingredients

**Base URL:** `/api/ingredients/`

| Method | URL | Description | Auth Required |
|---|---|---|---|
| GET | `/api/ingredients/` | List all ingredients | No |
| POST | `/api/ingredients/` | Create an ingredient | Yes |
| GET | `/api/ingredients/{id}/` | Retrieve an ingredient | No |
| PUT | `/api/ingredients/{id}/` | Update an ingredient | Yes |
| DELETE | `/api/ingredients/{id}/` | Delete an ingredient | Yes |

**Query params:** `?search=<name>`

**Fields:**

```json
{
  "id": 1,
  "name": "Morango",
  "portion": 50,
  "price": "3.50",
  "unit_of_measure": "g",
  "is_addon": false
}
```

---

## Recipients (Cup Sizes)

**Base URL:** `/api/recipients/`

| Method | URL | Description | Auth Required |
|---|---|---|---|
| GET | `/api/recipients/` | List all recipients | No |
| POST | `/api/recipients/` | Create a recipient | Yes |
| GET | `/api/recipients/{id}/` | Retrieve a recipient | No |
| PUT | `/api/recipients/{id}/` | Update a recipient | Yes |
| DELETE | `/api/recipients/{id}/` | Delete a recipient | Yes |

**Fields:**

```json
{
  "id": 1,
  "title": "300ml",
  "quantity_ml": 300,
  "price": "8.00",
  "stock": 100,
  "content": 2
}
```

---

## Final Cups

**Base URL:** `/api/final-cups/`

| Method | URL | Description | Auth Required |
|---|---|---|---|
| GET | `/api/final-cups/` | List all final cups | No |
| POST | `/api/final-cups/` | Create a final cup | Yes |
| GET | `/api/final-cups/{id}/` | Retrieve a final cup | No |
| PUT | `/api/final-cups/{id}/` | Update a final cup | Yes |
| DELETE | `/api/final-cups/{id}/` | Delete a final cup | Yes |

**Query params:** `?search=<name>`

**Fields:**

```json
{
  "id": 1,
  "name": "Açaí Tradicional",
  "price": "15.00",
  "recipient": 1,
  "recipient_data": { ... },
  "ingredient": [1, 2],
  "ingredient_data": [ ... ]
}
```

---

## Custom Cups

**Base URL:** `/api/custom-cups/`

| Method | URL | Description | Auth Required |
|---|---|---|---|
| GET | `/api/custom-cups/` | List all custom cups | No |
| POST | `/api/custom-cups/` | Create a custom cup | Yes |
| GET | `/api/custom-cups/{id}/` | Retrieve a custom cup | No |
| PUT | `/api/custom-cups/{id}/` | Update a custom cup | Yes |
| DELETE | `/api/custom-cups/{id}/` | Delete a custom cup | Yes |

> `price` is read-only and auto-calculated from the recipient and ingredients.

**Fields:**

```json
{
  "id": 1,
  "recipient": 1,
  "recipient_data": { ... },
  "ingredient": [1, 3],
  "ingredient_data": [ ... ],
  "price": "12.50"
}
```

---

## Combos

**Base URL:** `/api/combos/`

| Method | URL | Description | Auth Required |
|---|---|---|---|
| GET | `/api/combos/` | List all combos | No |
| POST | `/api/combos/` | Create a combo | Yes |
| GET | `/api/combos/{id}/` | Retrieve a combo | No |
| PUT | `/api/combos/{id}/` | Update a combo | Yes |
| DELETE | `/api/combos/{id}/` | Delete a combo | Yes |

**Query params:** `?search=<name>`

**Fields:**

```json
{
  "id": 1,
  "name": "Combo Família",
  "price": "45.00",
  "final_cup": [1, 2],
  "final_cup_data": [ ... ]
}
```

---

## Stock

**Base URL:** `/api/stock/`

| Method | URL | Description | Auth Required |
|---|---|---|---|
| GET | `/api/stock/` | List all stock entries | No |
| POST | `/api/stock/` | Add a stock entry | Yes |
| GET | `/api/stock/{id}/` | Retrieve a stock entry | No |
| PUT | `/api/stock/{id}/` | Update a stock entry | Yes |
| DELETE | `/api/stock/{id}/` | Delete a stock entry | Yes |
| GET | `/api/stock/low_stock/` | List items below threshold (5000 units) | No |

**Fields:**

```json
{
  "id": 1,
  "ingredient": 1,
  "ingredient_data": { ... },
  "quantity": "2000.00",
  "batch": "BATCH-001",
  "expiration_date": "2025-12-31",
  "supplier": 1,
  "supplier_data": { ... },
  "batch_price": "150.00"
}
```

---

## Daily Revenue

**Base URL:** `/api/daily-revenues/`

| Method | URL | Description | Auth Required |
|---|---|---|---|
| GET | `/api/daily-revenues/` | List revenue records for the user's establishment | Yes |
| POST | `/api/daily-revenues/` | Create a revenue record | Yes |
| GET | `/api/daily-revenues/{id}/` | Retrieve a revenue record | Yes |
| PUT | `/api/daily-revenues/{id}/` | Update a revenue record | Yes |
| DELETE | `/api/daily-revenues/{id}/` | Delete a revenue record | Yes |

> Records are created and updated automatically via signals. Manual creation is rarely needed.

**Query params:**

| Param | Format | Description |
|---|---|---|
| `start_date` | `YYYY-MM-DD` | Filter from this date |
| `end_date` | `YYYY-MM-DD` | Filter up to this date |

**Fields:**

```json
{
  "id": 1,
  "date": "2025-04-24T10:00:00Z",
  "total_amount": "320.50",
  "total_orders_count": 12,
  "establishment": 1
}
```

---

## Orders

**Base URL:** `/api/orders/`

| Method | URL | Description | Auth Required |
|---|---|---|---|
| GET | `/api/orders/` | List all orders (newest first) | No |
| POST | `/api/orders/` | Create an order | Yes |
| GET | `/api/orders/{id}/` | Retrieve order with full item detail | No |
| PUT | `/api/orders/{id}/` | Full update | Yes |
| PATCH | `/api/orders/{id}/` | Partial update (e.g., change status) | Yes |
| DELETE | `/api/orders/{id}/` | Delete an order | Yes |

> `establishment` and `responsible_person` are auto-set from the authenticated user on creation. Creating an order requires authentication even though GET is open, because `perform_create` reads `request.user`.

**Create / List fields:**

```json
{
  "id": 1,
  "customer": "João Silva",
  "order_date": "2025-04-24T10:00:00Z",
  "total_amount": "30.00",
  "establishment": 1,
  "status": "PENDING",
  "is_paid": false,
  "responsible_person": 2,
  "responsible_person_data": { ... },
  "payment_method": "PIX"
}
```

**Retrieve (detail) fields:**

```json
{
  "id": 1,
  "customer": "João Silva",
  "establishment": { ... },
  "order_date": "2025-04-24T10:00:00Z",
  "total_amount": "30.00",
  "status": "PENDING",
  "is_paid": false,
  "payment_method": "PIX",
  "items": [ ... ]
}
```

**Status choices:** `PENDING` | `IN_PROGRESS` | `COMPLETED` | `CANCELED`

**Payment method choices:** `PIX` | `CARD` | `CASH`

---

## Order Items

**Base URL:** `/api/order-items/`

| Method | URL | Description | Auth Required |
|---|---|---|---|
| GET | `/api/order-items/` | List all order items | No |
| POST | `/api/order-items/` | Add an item to an order | Yes |
| GET | `/api/order-items/{id}/` | Retrieve an order item | No |
| PUT | `/api/order-items/{id}/` | Update an order item | Yes |
| DELETE | `/api/order-items/{id}/` | Delete an order item | Yes |

> `unit_price` and `total_price` are auto-calculated via signal after save.

**Fields:**

```json
{
  "id": 1,
  "order": 1,
  "type": "FINAL_CUP",
  "final_cup": 2,
  "custom_cup": null,
  "combo": null,
  "quantity": 2,
  "unit_price": "15.00",
  "total_price": "30.00"
}
```

**Type choices:** `FINAL_CUP` | `CUSTOM_CUP` | `COMBO`

---

## Users

**Base URL:** `/api/users/`

| Method | URL | Description | Auth Required |
|---|---|---|---|
| GET | `/api/users/` | List all users | No |
| POST | `/api/users/` | Create a user | Yes |
| GET | `/api/users/{id}/` | Retrieve a user | No |
| PUT | `/api/users/{id}/` | Update a user | Yes |
| DELETE | `/api/users/{id}/` | Delete a user | Yes |
| GET | `/api/users/me/` | Get the currently authenticated user | Yes |

**Fields:**

```json
{
  "id": 1,
  "name": "Maria Souza",
  "email": "maria@example.com",
  "registration": 1042,
  "establishment": 1,
  "establishment_data": { ... }
}
```

---

## Addresses

**Base URL:** `/api/addresses/`

| Method | URL | Description | Auth Required |
|---|---|---|---|
| GET | `/api/addresses/` | List all addresses | No |
| POST | `/api/addresses/` | Create an address | Yes |
| GET | `/api/addresses/{id}/` | Retrieve an address | No |
| PUT | `/api/addresses/{id}/` | Update an address | Yes |
| DELETE | `/api/addresses/{id}/` | Delete an address | Yes |

**Query params:** `?search=<street|city|state>`, `?street=<street>`, `?city=<city>`, `?state=<state>`

**Fields:**

```json
{
  "id": 1,
  "street": "Rua das Flores",
  "number": "123",
  "city": "São Paulo",
  "state": "SP",
  "zip_code": "01310-100"
}
```

---

## Suppliers

**Base URL:** `/api/suppliers/`

| Method | URL | Description | Auth Required |
|---|---|---|---|
| GET | `/api/suppliers/` | List all suppliers | No |
| POST | `/api/suppliers/` | Create a supplier | Yes |
| GET | `/api/suppliers/{id}/` | Retrieve a supplier | No |
| PUT | `/api/suppliers/{id}/` | Update a supplier | Yes |
| DELETE | `/api/suppliers/{id}/` | Delete a supplier | Yes |

**Query params:** `?search=<name|legal_name|document>`, `?is_active=true`, `?type=MANUFACTURER`

**Supplier type choices:** `MANUFACTURER` | `DISTRIBUTOR` | `RETAILER` | `IMPORTER`

**Fields:**

```json
{
  "id": 1,
  "legal_name": "Frutas do Norte LTDA",
  "name": "FrutaNorte",
  "document": "12345678000195",
  "is_active": true,
  "type": "DISTRIBUTOR",
  "contact": 1,
  "address": 2,
  "contact_data": { ... },
  "address_data": { ... }
}
```

---

## Contacts

**Base URL:** `/api/contacts/`

| Method | URL | Description | Auth Required |
|---|---|---|---|
| GET | `/api/contacts/` | List all contacts | No |
| POST | `/api/contacts/` | Create a contact | Yes |
| GET | `/api/contacts/{id}/` | Retrieve a contact | No |
| PUT | `/api/contacts/{id}/` | Update a contact | Yes |
| DELETE | `/api/contacts/{id}/` | Delete a contact | Yes |

**Fields:**

```json
{
  "id": 1,
  "business_email": "contato@frutas.com",
  "financial_email": "financeiro@frutas.com",
  "phone_number": "11999990000",
  "whatsapp_number": "11999990000"
}
```
