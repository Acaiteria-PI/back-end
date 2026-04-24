# Referência da API

Todos os endpoints têm o prefixo `/api/`. A autenticação usa JWT — veja [autenticacao.md](./autenticacao.md).

> Documentação interativa disponível em `/api/swagger/` e `/api/redoc/`.

---

## Estabelecimentos

**URL base:** `/api/establishments/`

| Método | URL | Descrição | Auth Necessária |
|---|---|---|---|
| GET | `/api/establishments/` | Listar todos os estabelecimentos | Não |
| POST | `/api/establishments/` | Criar um estabelecimento | Sim |
| GET | `/api/establishments/{id}/` | Recuperar um estabelecimento | Não |
| PUT | `/api/establishments/{id}/` | Atualizar um estabelecimento | Sim |
| DELETE | `/api/establishments/{id}/` | Deletar um estabelecimento | Sim |

**Parâmetros de busca:** `?search=<name>`

**Campos:**

```json
{
  "id": 1,
  "name": "Pé de Açaí Centro",
  "cnpj": "12345678000195",
  "amount": "10000.00"
}
```

---

## Ingredientes

**URL base:** `/api/ingredients/`

| Método | URL | Descrição | Auth Necessária |
|---|---|---|---|
| GET | `/api/ingredients/` | Listar todos os ingredientes | Não |
| POST | `/api/ingredients/` | Criar um ingrediente | Sim |
| GET | `/api/ingredients/{id}/` | Recuperar um ingrediente | Não |
| PUT | `/api/ingredients/{id}/` | Atualizar um ingrediente | Sim |
| DELETE | `/api/ingredients/{id}/` | Deletar um ingrediente | Sim |

**Parâmetros de busca:** `?search=<name>`

**Campos:**

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

## Recipients (Tamanhos de Copo)

**URL base:** `/api/recipients/`

| Método | URL | Descrição | Auth Necessária |
|---|---|---|---|
| GET | `/api/recipients/` | Listar todos os recipients | Não |
| POST | `/api/recipients/` | Criar um recipient | Sim |
| GET | `/api/recipients/{id}/` | Recuperar um recipient | Não |
| PUT | `/api/recipients/{id}/` | Atualizar um recipient | Sim |
| DELETE | `/api/recipients/{id}/` | Deletar um recipient | Sim |

**Campos:**

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

## Copos Prontos

**URL base:** `/api/final-cups/`

| Método | URL | Descrição | Auth Necessária |
|---|---|---|---|
| GET | `/api/final-cups/` | Listar todos os copos prontos | Não |
| POST | `/api/final-cups/` | Criar um copo pronto | Sim |
| GET | `/api/final-cups/{id}/` | Recuperar um copo pronto | Não |
| PUT | `/api/final-cups/{id}/` | Atualizar um copo pronto | Sim |
| DELETE | `/api/final-cups/{id}/` | Deletar um copo pronto | Sim |

**Parâmetros de busca:** `?search=<name>`

**Campos:**

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

## Copos Customizados

**URL base:** `/api/custom-cups/`

| Método | URL | Descrição | Auth Necessária |
|---|---|---|---|
| GET | `/api/custom-cups/` | Listar todos os copos customizados | Não |
| POST | `/api/custom-cups/` | Criar um copo customizado | Sim |
| GET | `/api/custom-cups/{id}/` | Recuperar um copo customizado | Não |
| PUT | `/api/custom-cups/{id}/` | Atualizar um copo customizado | Sim |
| DELETE | `/api/custom-cups/{id}/` | Deletar um copo customizado | Sim |

> `price` é somente leitura e calculado automaticamente a partir do recipient e dos ingredientes.

**Campos:**

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

**URL base:** `/api/combos/`

| Método | URL | Descrição | Auth Necessária |
|---|---|---|---|
| GET | `/api/combos/` | Listar todos os combos | Não |
| POST | `/api/combos/` | Criar um combo | Sim |
| GET | `/api/combos/{id}/` | Recuperar um combo | Não |
| PUT | `/api/combos/{id}/` | Atualizar um combo | Sim |
| DELETE | `/api/combos/{id}/` | Deletar um combo | Sim |

**Parâmetros de busca:** `?search=<name>`

**Campos:**

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

## Estoque

**URL base:** `/api/stock/`

| Método | URL | Descrição | Auth Necessária |
|---|---|---|---|
| GET | `/api/stock/` | Listar todas as entradas de estoque | Não |
| POST | `/api/stock/` | Adicionar uma entrada de estoque | Sim |
| GET | `/api/stock/{id}/` | Recuperar uma entrada de estoque | Não |
| PUT | `/api/stock/{id}/` | Atualizar uma entrada de estoque | Sim |
| DELETE | `/api/stock/{id}/` | Deletar uma entrada de estoque | Sim |
| GET | `/api/stock/low_stock/` | Listar itens abaixo do limite (5000 unidades) | Não |

**Campos:**

```json
{
  "id": 1,
  "ingredient": 1,
  "ingredient_data": { ... },
  "quantity": "2000.00",
  "batch": "LOTE-001",
  "expiration_date": "2025-12-31",
  "supplier": 1,
  "supplier_data": { ... },
  "batch_price": "150.00"
}
```

---

## Faturamento Diário

**URL base:** `/api/daily-revenues/`

| Método | URL | Descrição | Auth Necessária |
|---|---|---|---|
| GET | `/api/daily-revenues/` | Listar registros de faturamento do estabelecimento do usuário | Sim |
| POST | `/api/daily-revenues/` | Criar um registro de faturamento | Sim |
| GET | `/api/daily-revenues/{id}/` | Recuperar um registro de faturamento | Sim |
| PUT | `/api/daily-revenues/{id}/` | Atualizar um registro de faturamento | Sim |
| DELETE | `/api/daily-revenues/{id}/` | Deletar um registro de faturamento | Sim |

> Os registros são criados e atualizados automaticamente via signals. A criação manual raramente é necessária.

**Parâmetros de busca:**

| Parâmetro | Formato | Descrição |
|---|---|---|
| `start_date` | `YYYY-MM-DD` | Filtrar a partir desta data |
| `end_date` | `YYYY-MM-DD` | Filtrar até esta data |

**Campos:**

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

## Pedidos

**URL base:** `/api/orders/`

| Método | URL | Descrição | Auth Necessária |
|---|---|---|---|
| GET | `/api/orders/` | Listar todos os pedidos (mais recentes primeiro) | Não |
| POST | `/api/orders/` | Criar um pedido | Sim |
| GET | `/api/orders/{id}/` | Recuperar pedido com detalhes completos dos itens | Não |
| PUT | `/api/orders/{id}/` | Atualização completa | Sim |
| PATCH | `/api/orders/{id}/` | Atualização parcial (ex.: alterar status) | Sim |
| DELETE | `/api/orders/{id}/` | Deletar um pedido | Sim |

> `establishment` e `responsible_person` são definidos automaticamente pelo usuário autenticado na criação. Criar um pedido requer autenticação mesmo que GET seja aberto, pois `perform_create` lê `request.user`.

**Campos de criação / listagem:**

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

**Campos de recuperação (detalhe):**

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

**Opções de status:** `PENDING` | `IN_PROGRESS` | `COMPLETED` | `CANCELED`

**Opções de método de pagamento:** `PIX` | `CARD` | `CASH`

---

## Itens de Pedido

**URL base:** `/api/order-items/`

| Método | URL | Descrição | Auth Necessária |
|---|---|---|---|
| GET | `/api/order-items/` | Listar todos os itens de pedido | Não |
| POST | `/api/order-items/` | Adicionar um item a um pedido | Sim |
| GET | `/api/order-items/{id}/` | Recuperar um item de pedido | Não |
| PUT | `/api/order-items/{id}/` | Atualizar um item de pedido | Sim |
| DELETE | `/api/order-items/{id}/` | Deletar um item de pedido | Sim |

> `unit_price` e `total_price` são calculados automaticamente via signal após o save.

**Campos:**

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

**Opções de tipo:** `FINAL_CUP` | `CUSTOM_CUP` | `COMBO`

---

## Usuários

**URL base:** `/api/users/`

| Método | URL | Descrição | Auth Necessária |
|---|---|---|---|
| GET | `/api/users/` | Listar todos os usuários | Não |
| POST | `/api/users/` | Criar um usuário | Sim |
| GET | `/api/users/{id}/` | Recuperar um usuário | Não |
| PUT | `/api/users/{id}/` | Atualizar um usuário | Sim |
| DELETE | `/api/users/{id}/` | Deletar um usuário | Sim |
| GET | `/api/users/me/` | Obter o usuário autenticado atual | Sim |

**Campos:**

```json
{
  "id": 1,
  "name": "Maria Souza",
  "email": "maria@exemplo.com",
  "registration": 1042,
  "establishment": 1,
  "establishment_data": { ... }
}
```

---

## Endereços

**URL base:** `/api/addresses/`

| Método | URL | Descrição | Auth Necessária |
|---|---|---|---|
| GET | `/api/addresses/` | Listar todos os endereços | Não |
| POST | `/api/addresses/` | Criar um endereço | Sim |
| GET | `/api/addresses/{id}/` | Recuperar um endereço | Não |
| PUT | `/api/addresses/{id}/` | Atualizar um endereço | Sim |
| DELETE | `/api/addresses/{id}/` | Deletar um endereço | Sim |

**Parâmetros de busca:** `?search=<street|city|state>`, `?street=<street>`, `?city=<city>`, `?state=<state>`

**Campos:**

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

## Fornecedores

**URL base:** `/api/suppliers/`

| Método | URL | Descrição | Auth Necessária |
|---|---|---|---|
| GET | `/api/suppliers/` | Listar todos os fornecedores | Não |
| POST | `/api/suppliers/` | Criar um fornecedor | Sim |
| GET | `/api/suppliers/{id}/` | Recuperar um fornecedor | Não |
| PUT | `/api/suppliers/{id}/` | Atualizar um fornecedor | Sim |
| DELETE | `/api/suppliers/{id}/` | Deletar um fornecedor | Sim |

**Parâmetros de busca:** `?search=<name|legal_name|document>`, `?is_active=true`, `?type=MANUFACTURER`

**Opções de tipo de fornecedor:** `MANUFACTURER` | `DISTRIBUTOR` | `RETAILER` | `IMPORTER`

**Campos:**

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

## Contatos

**URL base:** `/api/contacts/`

| Método | URL | Descrição | Auth Necessária |
|---|---|---|---|
| GET | `/api/contacts/` | Listar todos os contatos | Não |
| POST | `/api/contacts/` | Criar um contato | Sim |
| GET | `/api/contacts/{id}/` | Recuperar um contato | Não |
| PUT | `/api/contacts/{id}/` | Atualizar um contato | Sim |
| DELETE | `/api/contacts/{id}/` | Deletar um contato | Sim |

**Campos:**

```json
{
  "id": 1,
  "business_email": "contato@frutas.com",
  "financial_email": "financeiro@frutas.com",
  "phone_number": "11999990000",
  "whatsapp_number": "11999990000"
}
```
