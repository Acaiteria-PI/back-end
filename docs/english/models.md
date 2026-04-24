# Data Models

This document describes all database models and their relationships.

---

## Address

**App:** `core.adress`

| Field | Type | Description |
|---|---|---|
| `id` | AutoField | Primary key |
| `street` | CharField(255) | Street name |
| `number` | CharField(20) | Street number |
| `city` | CharField(100) | City |
| `state` | CharField(100) | State |
| `zip_code` | CharField(20) | ZIP / postal code |

---

## Establishment

**App:** `core.establishment`

| Field | Type | Description |
|---|---|---|
| `id` | AutoField | Primary key |
| `name` | CharField(255) | Establishment name |
| `cnpj` | CharField(14) | Brazilian tax ID |
| `amount` | DecimalField | Current balance / cash amount |

---

## User

**App:** `core.users`

Extends Django's `AbstractUser`. The `username` field is removed.

| Field | Type | Description |
|---|---|---|
| `id` | AutoField | Primary key |
| `email` | EmailField | Unique — used as login |
| `name` | CharField(255) | Display name |
| `registration` | IntegerField | Optional unique employee ID |
| `establishment` | FK → Establishment | The shop this user belongs to |

---

## Ingredient

**App:** `core.establishment`

| Field | Type | Description |
|---|---|---|
| `id` | AutoField | Primary key |
| `name` | CharField(45) | Ingredient name |
| `portion` | IntegerField | Default portion size |
| `price` | DecimalField | Price per portion |
| `unit_of_measure` | CharField(20) | Unit (e.g., `g`, `ml`) — default `g` |
| `is_addon` | BooleanField | Whether it's an optional add-on |

---

## Recipient (Cup Size)

**App:** `core.establishment`

Represents a physical cup size that holds a base ingredient (e.g., açaí base).

| Field | Type | Description |
|---|---|---|
| `id` | AutoField | Primary key |
| `title` | CharField(45) | Size name (e.g., "300ml") |
| `quantity_ml` | IntegerField | Volume in milliliters |
| `price` | DecimalField | Price of this cup size |
| `stock` | IntegerField | Available stock count |
| `content` | FK → Ingredient | The base ingredient this cup contains |

---

## FinalCup (Ready-made Cup)

**App:** `core.establishment`

A pre-defined cup product with a fixed set of ingredients.

| Field | Type | Description |
|---|---|---|
| `id` | AutoField | Primary key |
| `name` | CharField(45) | Product name |
| `price` | DecimalField | Selling price |
| `recipient` | FK → Recipient | The cup size used |
| `ingredient` | M2M → Ingredient | Toppings / ingredients included |

---

## CustomCup (Custom-built Cup)

**App:** `core.establishment`

A cup assembled by the customer with a chosen recipient and ingredients. Price is **auto-calculated** via signal.

| Field | Type | Description |
|---|---|---|
| `id` | AutoField | Primary key |
| `price` | DecimalField | Auto-calculated (read-only) |
| `recipient` | FK → Recipient | The cup size chosen |
| `ingredient` | M2M → Ingredient | Chosen toppings |

> Price = `recipient.price` + sum of all `ingredient.price` values. Recalculated automatically whenever ingredients or recipient change.

---

## Combo

**App:** `core.establishment`

A bundle of multiple FinalCups sold together at a fixed price.

| Field | Type | Description |
|---|---|---|
| `id` | AutoField | Primary key |
| `name` | CharField(45) | Combo name |
| `price` | DecimalField | Combo price |
| `final_cup` | M2M → FinalCup | Cups included in this combo |

---

## Stock

**App:** `core.establishment`

Tracks ingredient inventory by batch, with expiration date for FIFO deduction.

| Field | Type | Description |
|---|---|---|
| `id` | AutoField | Primary key |
| `ingredient` | FK → Ingredient | The ingredient in stock |
| `quantity` | DecimalField | Current quantity available |
| `batch` | CharField(100) | Batch identifier |
| `expiration_date` | DateField | Expiration date (used for FIFO ordering) |
| `supplier` | FK → Supplier | Supplier of this batch (nullable) |
| `batch_price` | DecimalField | Total cost of this batch |

---

## DailyRevenue

**App:** `core.establishment`

Aggregated revenue record per establishment per day. Managed automatically via signals.

| Field | Type | Description |
|---|---|---|
| `id` | AutoField | Primary key |
| `date` | DateTimeField | Auto-set on creation |
| `total_amount` | DecimalField | Total revenue for the day |
| `total_orders_count` | IntegerField | Number of paid orders |
| `establishment` | FK → Establishment | The establishment this record belongs to |

---

## Supplier

**App:** `core.supplier`

| Field | Type | Description |
|---|---|---|
| `id` | AutoField | Primary key |
| `legal_name` | CharField(200) | Full legal name |
| `name` | CharField(100) | Trade name |
| `document` | CharField(100) | CNPJ or CPF |
| `is_active` | BooleanField | Whether the supplier is active |
| `type` | CharField | `MANUFACTURER`, `DISTRIBUTOR`, `RETAILER`, or `IMPORTER` |
| `contact` | OneToOne → Contact | Contact info (nullable) |
| `address` | FK → Address | Supplier address (nullable) |

---

## Contact

**App:** `core.supplier`

| Field | Type | Description |
|---|---|---|
| `id` | AutoField | Primary key |
| `business_email` | EmailField | General business email |
| `financial_email` | EmailField | Finance department email |
| `phone_number` | CharField(15) | Phone number |
| `whatsapp_number` | CharField(15) | WhatsApp number |

---

## Order

**App:** `core.orders`

| Field | Type | Description |
|---|---|---|
| `id` | AutoField | Primary key |
| `customer` | CharField(45) | Customer name |
| `order_date` | DateTimeField | Auto-set on creation |
| `status` | CharField | `PENDING`, `IN_PROGRESS`, `COMPLETED`, `CANCELED` — default `PENDING` |
| `establishment` | FK → Establishment | Auto-set from the logged-in user |
| `responsible_person` | FK → User | Auto-set from the logged-in user |
| `total_amount` | DecimalField | Auto-calculated from order items — default `0.00` |
| `is_paid` | BooleanField | Payment status — default `False` |
| `payment_method` | CharField | `PIX`, `CARD`, or `CASH` (nullable) |

---

## OrderItem

**App:** `core.orders`

Each item in an order. Exactly one of `final_cup`, `custom_cup`, or `combo` should be set depending on `type`.

| Field | Type | Description |
|---|---|---|
| `id` | AutoField | Primary key |
| `order` | FK → Order | Parent order |
| `type` | CharField | `FINAL_CUP`, `CUSTOM_CUP`, or `COMBO` |
| `final_cup` | FK → FinalCup | Set when type is `FINAL_CUP` (nullable) |
| `custom_cup` | FK → CustomCup | Set when type is `CUSTOM_CUP` (nullable) |
| `combo` | FK → Combo | Set when type is `COMBO` (nullable) |
| `quantity` | PositiveIntegerField | Quantity ordered |
| `unit_price` | DecimalField | Auto-set from the product price |
| `total_price` | DecimalField | `unit_price × quantity` — auto-calculated |

---

## Relationships Summary

```
Establishment ──< User
Establishment ──< Order
Establishment ──< DailyRevenue

Ingredient >──< FinalCup (M2M)
Ingredient >──< CustomCup (M2M)
Ingredient ──< Stock
Ingredient ──< Recipient (content FK)

Recipient ──< FinalCup
Recipient ──< CustomCup

FinalCup >──< Combo (M2M)

Order ──< OrderItem
OrderItem ──> FinalCup | CustomCup | Combo

Supplier ──< Stock
Supplier ── Contact (OneToOne)
Supplier ──> Address
```
