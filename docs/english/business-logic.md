# Business Logic

This document describes the automated behaviors of the API that integrators should be aware of.

---

## Order Item Pricing

Prices are **never manually set** on order items. When you create or update an `OrderItem`, the API automatically:

- Sets `unit_price` based on the linked product (FinalCup, CustomCup, or Combo)
- Calculates `total_price = unit_price × quantity`
- Updates the parent `Order.total_amount` accordingly

Do not send `unit_price` or `total_price` in your request body — they will always be overwritten.

---

## Stock Deduction

When an order's `status` is changed to `IN_PROGRESS`, the API automatically deducts the required ingredient quantities from stock.

- If any ingredient has insufficient stock, the entire operation is rolled back and an error is returned.
- Stock is **not** deducted at any other status transition.

---

## Custom Cup Pricing

The `price` field on a `CustomCup` is read-only and always auto-calculated as:

```
price = recipient price + sum of all ingredient prices
```

It updates automatically whenever the recipient or ingredients are changed. You cannot set it manually.

---

## Daily Revenue

Revenue records are managed automatically:

- When an order's `is_paid` is set to `true`, the order's total is added to the daily revenue record for that establishment and day.
- When an order is `CANCELED`, its total is subtracted from the corresponding daily revenue record.

You do not need to interact with the `/api/daily-revenues/` endpoint directly — it reflects the state of your orders automatically.
