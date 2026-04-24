# Lógica de Negócio

Este documento descreve os comportamentos automatizados da API que os integradores precisam conhecer.

---

## Precificação de Itens do Pedido

Os preços **nunca são definidos manualmente** nos itens de pedido. Ao criar ou atualizar um `OrderItem`, a API automaticamente:

- Define `unit_price` com base no produto vinculado (FinalCup, CustomCup ou Combo)
- Calcula `total_price = unit_price × quantity`
- Atualiza o `total_amount` do `Order` pai correspondente

Não envie `unit_price` ou `total_price` no corpo da requisição — eles sempre serão sobrescritos.

---

## Dedução de Estoque

Quando o `status` de um pedido é alterado para `IN_PROGRESS`, a API deduz automaticamente as quantidades necessárias de ingredientes do estoque.

- Se algum ingrediente tiver estoque insuficiente, toda a operação é revertida e um erro é retornado.
- O estoque **não** é deduzido em nenhuma outra transição de status.

---

## Precificação do Copo Customizado

O campo `price` de um `CustomCup` é somente leitura e sempre calculado automaticamente como:

```
preço = preço do recipient + soma dos preços de todos os ingredientes
```

Ele é atualizado automaticamente sempre que o recipient ou os ingredientes forem alterados. Não é possível defini-lo manualmente.

---

## Faturamento Diário

Os registros de faturamento são gerenciados automaticamente:

- Quando `is_paid` de um pedido é definido como `true`, o total do pedido é adicionado ao registro de faturamento diário do estabelecimento correspondente.
- Quando um pedido é `CANCELED`, seu total é subtraído do registro de faturamento diário correspondente.

Não é necessário interagir diretamente com o endpoint `/api/daily-revenues/` — ele reflete o estado dos seus pedidos automaticamente.
