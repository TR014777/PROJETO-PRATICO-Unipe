produtos = []
precos = []
quantidades = []
cupons_disponiveis = {
    "DESC5": 5.00,
    "DESC10": 10.00,  # Desconto de R$ 10,00
    "DESC20": 20.00,  # Desconto de R$ 20,00
    "DESC30": 30.00,  # Desconto de R$ 30,00
}
cupons_ativados = []

def registrar_mercadorias():
    ativo = True
    while(ativo == True):
        produto = input("Digite qual é o produto(exemplo: Miojo, Pasta de Dente):\n")
        preco = float(input("Digite o preço do produto(exemplo: 3, 5.90, 12.34):\n"))
        quantidade = int(input("Digite quantas unidades:\n"))
        produtos.append(produto)
        precos.append(preco * quantidade)
        quantidades.append(quantidade)
        continuar = input("Deseja continuar? \nDigite 's' se sim. caso não, digite qualquer tecla.\n")
        match continuar:
            case 's':
                pass
            case _:
                ativo = False
                mostrar_lista()

def remover_lista():
    item_desejado = input("Qual produto você deseja remover?")

    indice = produtos.index(item_desejado)

    produtos.pop(indice)
    quantidades.pop(indice)
    precos.pop(indice)
    mostrar_lista()

def calcular_desconto():
    desconto_total = 0
    for cupom in cupons_ativados:
        desconto_total += cupons_disponiveis[cupom]
    return desconto_total

def metodo_de_pagamento():
    print("\nQual metodo de pagamento deseja utilizar?")
    print("1. Cartão Débito ou Crédito.")
    print("2. Pagamento por Pix.")
    print("3. Pagamento com dinheiro.")
    print("4. Digite 'voltar' caso não queira pagar agora.\n")
    resposta = input()

    match resposta:
        case '1':
            print("\nDeseja utilizar Débito ou Crédito?")
            print("1. Débito.")
            print("2. Crédito.\n")
            cartao = input("\n")

            match cartao:
                case '1' | '2':
                    print("\nNos informe o número de seu cartão. Não deve conter os espaçamentos entre os números.\n")
                    while True:
                            try:
                                numero_cartao = int(input())
                                if 0000000000000000 < numero_cartao < 9999999999999999:
                                    print("\nPor favor, digite a data de vencimento do seu cartão.\n")
                                    mes = int(input("Mês: "))
                                    ano = int(input("Ano: "))
                                    if 0 < mes < 13:
                                        pass
                                    if ano <= 2025:
                                        pass
                                    cvv = int(input("\nAgora, digite o seu CVV.\n"))
                                    if 100 < cvv < 999:
                                        pass
                                    conclusao = input("\nSuas credenciais estão corretas, deseja concluir a compra? Digite s para sim e n para não.\n")
                                    match conclusao:
                                        case 's':
                                            print("\nSua compra foi realizada com sucesso! Muito obrigado por comprar conosco!")
                                            break
                                        case '_':
                                            break
                                    if ano == 2025 and mes < 6:
                                        print("\nO seu cartão está vencido.\n")
                                        metodo_de_pagamento()
                                print("\nO número do cartão é inválido.")
                            except ValueError:
                                print("\nNão foi digitado um número.\n")
                                metodo_de_pagamento()
        case '2':
            pix = input('\nDeseja utilizar Pix como seu método de pagamento? Digite S para sim e N para não.\n')
            match pix:
                case 's':
                    input("\nCopie e cole o link a seguir e finalize a compra: 00020101021126580014br.gov.bcb.pix01366b506d59-4899-404b-a741-cca75b367e935204000053039865802BR5918ANDRE L M OLIVEIRA6011JOAO PESSOA62070503***63048B14\n")
                    print("Sua compra foi realizada com sucesso! Muito obrigado por comprar conosco!")
                case 'n':
                    metodo_de_pagamento()
        case 'voltar':
            mostrar_lista()
   
def mostrar_lista():
    for produto, quantidade, preco in zip(produtos, quantidades, precos):
        print(f"{produto} [{quantidade} unidade(s)]: R$ {preco:.2f}")
    total = 0
    for preco in precos:
        total += preco
    desconto = calcular_desconto()
    desconto_total = total - desconto
    print("_________________________________")
    print(f"Desconto: R${desconto:.2f}")
    print(f'\nTotal: R${desconto_total:.2f}')
    print("_________________________________")
    mostrar_opcoes()

def mostrar_opcoes():
    print("Digite o número para selecionar a lista ordenada abaixo:")
    print("1. Adicionar cupom de desconto")
    print("2. Adicionar mais um item à lista")
    print("3. Remover item da lista")
    print("4. Prosseguir com o pagamento.")
    print("5. Cancelar a compra.\n")
    resposta = input("Ou Digite qualquer tecla para finalizar a compra.\n")

    match resposta:
        case '1':
            adicionar_cupom()
        case '2':
            registrar_mercadorias()
        case '3':
            remover_lista()
        case '4':
            metodo_de_pagamento()
        case '5':
            print("Compra cancelada.")
            pass
            ## irá cancelar a compra
        case _:
            metodo_de_pagamento()

def adicionar_cupom():
    cupom = input("Adicione o seu cupom:\n")
    total = sum(precos)

    if cupom in cupons_disponiveis and cupom not in cupons_ativados:
        desconto = cupons_disponiveis[cupom]
        if desconto >= total:
            print(f"O cupom {cupom} não pode ser aplicado. O desconto excede o valor da compra.")
        else:
            cupons_ativados.append(cupom)
            print(f"O cupom {cupom} foi adicionado! Desconto de R${desconto:.2f}.")
    else:
        print(f"O cupom {cupom} é inválido ou já foi usado.")
    mostrar_lista()

if __name__ == "__main__":
    registrar_mercadorias()