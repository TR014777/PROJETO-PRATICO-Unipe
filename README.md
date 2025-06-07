
# 🛒 Sistema de Caixa de Supermercado (Python)

Este é um programa de terminal que simula um sistema de **caixa de supermercado**, permitindo gerenciar compras com funcionalidades como aplicação de cupons de desconto, adição e remoção de produtos, além de múltiplas formas de pagamento.

## ✅ Funcionalidades

1. **Adicionar cupom de desconto**
   - Aceita cupons pré-definidos.
   - Cada cupom só pode ser usado uma vez.
   - Cupons não são aplicados se o desconto for maior que o total da compra.

2. **Adicionar item à lista**
   - O usuário pode adicionar produtos informando nome, quantidade e preço.
   - Os valores são acumulados na lista de compras.

3. **Remover item da lista**
   - O usuário pode remover produtos já adicionados, desde que existam na lista.

4. **Cancelar a compra**
   - Apaga toda a lista de compras e finaliza o processo.

5. **Formas de pagamento**
   - Cartão (débito ou crédito): simulação de inserção de dados do cartão.
   - Pix: simula chave para pagamento.
   - Dinheiro: calcula troco com detalhamento em notas e moedas.

## 💰 Cupons disponíveis

| Cupom   | Desconto |
|---------|----------|
| DESC5   | R$5,00   |
| DESC10  | R$10,00  |
| DESC20  | R$20,00  |
| DESC30  | R$30,00  |

## 🧾 Exemplo de fluxo

1. Adicionar produtos.
2. Ver lista com total.
3. Inserir cupom (opcional).
4. Escolher ação: adicionar/remover item, cancelar ou pagar.
5. Escolher método de pagamento.
6. Finalizar compra.

## 📌 Observações

- O sistema lida com entradas inválidas com tratamento de erros.
- O troco é calculado com divisão por notas e moedas.
- O código foi dividido em funções para manter clareza e modularidade.
