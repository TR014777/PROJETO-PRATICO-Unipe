produtos = []
precos = []
ativo = True
while(ativo == True):
    produto = input("Digite qual é o produto(exemplo: Miojo, Pasta de Dente):\n")
    preco = float(input("Digite o preço do produto(exemplo: 3, 5.90, 12.34):\n"))
    produtos.append(produto)
    precos.append(preco)
    continuar = input("Deseja continuar? \nDigite 's' se sim. caso não, digite qualquer tecla.\n")
    match continuar:
        case 's':
            pass
        case _:
            ativo = False

for produto, preco in zip(produtos, precos):
    print(f"{produto}: R$ {preco:.2f}")
total = 0
for preco in precos:
    total += preco
print("_________________________________")
print(f'\nTotal: R${total:.2f}')
print("_________________________________")

print("Digite o número para selecionar a lista ordenada abaixo:")
print("1. Adicionar cupom de desconto")
print("2. Remover item da lista")
print("3. Cancelar a compra\n")
respota = input("Ou Digite qualquer tecla para finalizar a compra.\n")


match respota:
    case 1:
        pass
        ## basicamente vai adicionar um cupom e ganhar um desconto
    case 2:
        pass
        ## permite remover algum item da lista
    case 3:
        pass
        ## irá cancelar a compra
    case _:
        pass
        ## ao teclar qualquer tecla, finaliza a compra e seleciona o metodo de pagamento.
