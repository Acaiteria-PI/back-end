# Modelos de Dados

Este documento descreve todos os modelos do banco de dados e seus relacionamentos.

---

## Address (Endereço)

**App:** `core.adress`

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | AutoField | Chave primária |
| `street` | CharField(255) | Nome da rua |
| `number` | CharField(20) | Número |
| `city` | CharField(100) | Cidade |
| `state` | CharField(100) | Estado |
| `zip_code` | CharField(20) | CEP |

---

## Establishment (Estabelecimento)

**App:** `core.establishment`

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | AutoField | Chave primária |
| `name` | CharField(255) | Nome do estabelecimento |
| `cnpj` | CharField(14) | CNPJ |
| `amount` | DecimalField | Saldo / valor em caixa |

---

## User (Usuário)

**App:** `core.users`

Estende o `AbstractUser` do Django. O campo `username` foi removido.

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | AutoField | Chave primária |
| `email` | EmailField | Único — usado para login |
| `name` | CharField(255) | Nome de exibição |
| `registration` | IntegerField | Matrícula única do funcionário (opcional) |
| `establishment` | FK → Establishment | A loja à qual o usuário pertence |

---

## Ingredient (Ingrediente)

**App:** `core.establishment`

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | AutoField | Chave primária |
| `name` | CharField(45) | Nome do ingrediente |
| `portion` | IntegerField | Tamanho da porção padrão |
| `price` | DecimalField | Preço por porção |
| `unit_of_measure` | CharField(20) | Unidade (ex.: `g`, `ml`) — padrão `g` |
| `is_addon` | BooleanField | Se é um adicional opcional |

---

## Recipient (Tamanho do Copo)

**App:** `core.establishment`

Representa um tamanho físico de copo que contém um ingrediente base (ex.: base de açaí).

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | AutoField | Chave primária |
| `title` | CharField(45) | Nome do tamanho (ex.: "300ml") |
| `quantity_ml` | IntegerField | Volume em mililitros |
| `price` | DecimalField | Preço deste tamanho de copo |
| `stock` | IntegerField | Quantidade disponível em estoque |
| `content` | FK → Ingredient | O ingrediente base que este copo contém |

---

## FinalCup (Copo Pronto)

**App:** `core.establishment`

Um produto de copo pré-definido com um conjunto fixo de ingredientes.

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | AutoField | Chave primária |
| `name` | CharField(45) | Nome do produto |
| `price` | DecimalField | Preço de venda |
| `recipient` | FK → Recipient | O tamanho de copo utilizado |
| `ingredient` | M2M → Ingredient | Complementos / ingredientes incluídos |

---

## CustomCup (Copo Customizado)

**App:** `core.establishment`

Um copo montado pelo cliente com um recipient e ingredientes escolhidos. O preço é **calculado automaticamente** via signal.

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | AutoField | Chave primária |
| `price` | DecimalField | Calculado automaticamente (somente leitura) |
| `recipient` | FK → Recipient | O tamanho de copo escolhido |
| `ingredient` | M2M → Ingredient | Complementos escolhidos |

> Preço = `recipient.price` + soma de todos os `ingredient.price`. Recalculado automaticamente sempre que os ingredientes ou o recipient forem alterados.

---

## Combo

**App:** `core.establishment`

Um conjunto de múltiplos CoposProntos vendidos juntos por um preço fixo.

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | AutoField | Chave primária |
| `name` | CharField(45) | Nome do combo |
| `price` | DecimalField | Preço do combo |
| `final_cup` | M2M → FinalCup | Copos incluídos neste combo |

---

## Stock (Estoque)

**App:** `core.establishment`

Rastreia o inventário de ingredientes por lote, com data de validade para dedução FIFO.

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | AutoField | Chave primária |
| `ingredient` | FK → Ingredient | O ingrediente em estoque |
| `quantity` | DecimalField | Quantidade disponível atual |
| `batch` | CharField(100) | Identificador do lote |
| `expiration_date` | DateField | Data de validade (usada para ordenação FIFO) |
| `supplier` | FK → Supplier | Fornecedor deste lote (nullable) |
| `batch_price` | DecimalField | Custo total deste lote |

---

## DailyRevenue (Faturamento Diário)

**App:** `core.establishment`

Registro agregado de faturamento por estabelecimento por dia. Gerenciado automaticamente via signals.

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | AutoField | Chave primária |
| `date` | DateTimeField | Definido automaticamente na criação |
| `total_amount` | DecimalField | Faturamento total do dia |
| `total_orders_count` | IntegerField | Número de pedidos pagos |
| `establishment` | FK → Establishment | O estabelecimento ao qual este registro pertence |

---

## Supplier (Fornecedor)

**App:** `core.supplier`

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | AutoField | Chave primária |
| `legal_name` | CharField(200) | Razão social |
| `name` | CharField(100) | Nome fantasia |
| `document` | CharField(100) | CNPJ ou CPF |
| `is_active` | BooleanField | Se o fornecedor está ativo |
| `type` | CharField | `MANUFACTURER`, `DISTRIBUTOR`, `RETAILER` ou `IMPORTER` |
| `contact` | OneToOne → Contact | Informações de contato (nullable) |
| `address` | FK → Address | Endereço do fornecedor (nullable) |

---

## Contact (Contato)

**App:** `core.supplier`

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | AutoField | Chave primária |
| `business_email` | EmailField | E-mail comercial geral |
| `financial_email` | EmailField | E-mail do departamento financeiro |
| `phone_number` | CharField(15) | Telefone |
| `whatsapp_number` | CharField(15) | WhatsApp |

---

## Order (Pedido)

**App:** `core.orders`

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | AutoField | Chave primária |
| `customer` | CharField(45) | Nome do cliente |
| `order_date` | DateTimeField | Definido automaticamente na criação |
| `status` | CharField | `PENDING`, `IN_PROGRESS`, `COMPLETED`, `CANCELED` — padrão `PENDING` |
| `establishment` | FK → Establishment | Definido automaticamente pelo usuário logado |
| `responsible_person` | FK → User | Definido automaticamente pelo usuário logado |
| `total_amount` | DecimalField | Calculado automaticamente a partir dos itens — padrão `0.00` |
| `is_paid` | BooleanField | Status de pagamento — padrão `False` |
| `payment_method` | CharField | `PIX`, `CARD` ou `CASH` (nullable) |

---

## OrderItem (Item do Pedido)

**App:** `core.orders`

Cada item de um pedido. Exatamente um entre `final_cup`, `custom_cup` ou `combo` deve ser preenchido de acordo com o `type`.

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | AutoField | Chave primária |
| `order` | FK → Order | Pedido pai |
| `type` | CharField | `FINAL_CUP`, `CUSTOM_CUP` ou `COMBO` |
| `final_cup` | FK → FinalCup | Preenchido quando type é `FINAL_CUP` (nullable) |
| `custom_cup` | FK → CustomCup | Preenchido quando type é `CUSTOM_CUP` (nullable) |
| `combo` | FK → Combo | Preenchido quando type é `COMBO` (nullable) |
| `quantity` | PositiveIntegerField | Quantidade pedida |
| `unit_price` | DecimalField | Definido automaticamente a partir do preço do produto |
| `total_price` | DecimalField | `unit_price × quantity` — calculado automaticamente |

---

## Resumo dos Relacionamentos

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
