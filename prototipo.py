## criando listas para armazenar dados dos produtos 
produtos = []
precos = []
quantidades = []

## um dicionário para armazenar os cupons com seus respectivos valores
cupons_disponiveis = {
    "DESC5": 5.00,
    "DESC10": 10.00,  # Desconto de R$ 10,00
    "DESC20": 20.00,  # Desconto de R$ 20,00
    "DESC30": 30.00,  # Desconto de R$ 30,00
}
cupons_ativados = []

## função que vai criar a lista dos produtos e adicionar os item com preço e quantidade
def registrar_mercadorias():
    ativo = True
    while(ativo == True):
        produto = input("Digite qual é o produto(exemplo: Miojo, Pasta de Dente):\n")
        while True:
            try:
                while True:
                    preco = float(input("Digite o preço do produto(exemplo: 3, 5.90, 12.34):\n"))
                    if preco >= 0:
                        break
                    print("Preço inválido.")
                break
            except ValueError:
                print("Valor inválido.")
        while True:
            try:
                while True:
                    quantidade = int(input("Digite quantas unidades:\n"))
                    if quantidade >= 1:
                        break
                    print("Quantidade inválida.")
                break
            except ValueError:
                print("Valor inválido.")
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


## função que remove um item da lista
def remover_lista():
    ativo = True
    while ativo == True:
        item_desejado = input("Qual produto você deseja remover? (OBS.: O produto precisa existir na lista para remover)\n")

        if item_desejado in produtos:
            indice = produtos.index(item_desejado)
            produtos.pop(indice)
            quantidades.pop(indice)
            precos.pop(indice)
            print(f"{item_desejado} foi removido com sucesso!")
            ativo = False
            mostrar_lista()
        else:
            print(f'O produto "{item_desejado}" não foi encontrado na lista.')

## função para calcular os descontos
def calcular_desconto():
    desconto_total = 0
    for cupom in cupons_ativados:
        desconto_total += cupons_disponiveis[cupom]
    return desconto_total


## obs.: esta função abaixo foi desenvolvida inteiramente por andré, decidi manter ela assim corrigindo e adicionando algumas coisas, mas
#  funciona perfeitamente, apesar de imensa. vou comentar a medida que vou descendo a função. - Daniel

## função do método de pagamento
def metodo_de_pagamento():
    print("\nQual metodo de pagamento deseja utilizar?")
    print("1. Cartão Débito ou Crédito.")
    print("2. Pagamento por Pix.")
    print("3. Pagamento com dinheiro.")
    print("4. Digite 'voltar' caso não queira pagar agora.\n")
    resposta = input()

    match resposta:
        ## caso seja cartão
        case '1':
            print("\nDeseja utilizar Débito ou Crédito?")
            print("1. Débito.")
            print("2. Crédito.\n")
            cartao = input("\n")

            match cartao:
                case '1' | '2':
                    ## armazenar as credenciais do cartão
                    print("\nNos informe o número de seu cartão. Não deve conter os espaçamentos entre os números.\n")
                    ativo = True
                    while ativo == True:
                            try:
                                numero_cartao = input()
                                if len(numero_cartao) == 16 and numero_cartao.isdigit(): ##0000000000000000
                                    print("\nPor favor, digite a data de vencimento do seu cartão.\n")
                                    while True:
                                        try:
                                            mes = int(input("Mês: "))
                                            if 0 < mes < 13:
                                                ano = int(input("Ano: "))
                                                if ano >= 2025:
                                                    cvv = input("\nAgora, digite o seu CVV.\n")
                                                    if 3 == len(cvv):
                                                        break
                                                    else:
                                                        print("CVV inválido.")
                                                else:
                                                    print("\nO seu cartão está vencido ou ano inválido.\n")
                                            else:
                                                print("Mês inválido.")
                                                
                                        except ValueError:
                                            print("Credências inválidas.")
                                    
                                    conclusao = input('\nSuas credenciais estão corretas, deseja concluir a compra? \nPressione Enter para continuar ou Digite "n" para voltar.\n')
                                    match conclusao:
                                        case '_':
                                            print("\nSua compra foi realizada com sucesso! Muito obrigado por comprar conosco!")
                                            break
                                        
                                        case 'n':
                                            ativo = False
                                            metodo_de_pagamento()
                                else:
                                    print("\nO número do cartão é inválido.")
                            except ValueError:
                                print("\nNão foi digitado o número do cartão.\n")
                                metodo_de_pagamento()
        case '2':
            ## caso escolha o pix
            pix = input('\nDeseja utilizar Pix como seu método de pagamento? Digite N para não ou digite qualquer tecla para confirmar.\n')
            match pix:
                case '_':
                    input("\nCopie e cole o link a seguir e finalize a compra:\n00020126360014BR.GOV.BCB.PIX0114+551199999999520400005303986540510.005802BR5911FULANO DE TAL6009SAO PAULO62140510TESTE1234566304ABCD\n")
                    print("Sua compra foi realizada com sucesso! Muito obrigado por comprar conosco!")
                case 'n' | 'N':
                    metodo_de_pagamento()
        case '3':
            ## caso escolha em dinheiro
            desconto_total, desconto = calcular_total_com_desconto()
            print("______________________________\n")
            print(f"Desconto: R${desconto:.2f}")
            print(f"Total a pagar: R${desconto_total:.2f}")
            print("______________________________\n")
            while True:
                try:
                    ## temos algumas condições para o pagamento caso os valores sejam diferentes ou iguais
                    dinheiro_a_pagar = float(input("Digite o quanto foi pago: "))
                    if dinheiro_a_pagar == desconto_total:
                        ## se pagou tudo, então finaliza aqui mesmo
                        print("Sua compra foi realizada com sucesso! Muito obrigado por comprar conosco!")
                        break
                    elif dinheiro_a_pagar >= desconto_total:
                        ## se pagou mais que devia, então vai calcular o troco e devolver a quantia
                        calcular_troco(dinheiro_a_pagar)
                        print("Sua compra foi realizada com sucesso! Muito obrigado por comprar conosco!")
                        break
                    elif dinheiro_a_pagar < desconto_total and dinheiro_a_pagar > 0:
                        ## se pagou menos que devia, então vai pedir a quantia que precisa para o pagamento
                        while True:
                            dinheiro_faltando = desconto_total - dinheiro_a_pagar
                            try:
                                dinheiro_faltando_pago = float(input(f"Dinheiro faltando. Acrescente mais R${dinheiro_faltando:.2f}, digite o valor faltando.\n\n"))
                                if dinheiro_faltando - dinheiro_faltando_pago == 0:
                                    print("Sua compra foi realizada com sucesso! Muito obrigado por comprar conosco!")
                                    break
                            except ValueError:
                                print("Valor inválido.")
                        break
                    else:
                        print("Não digite números inválidos.")
                except ValueError:
                    print("Valor inválido.")

        case 'voltar':
            mostrar_lista()

## função para calcular o total com base em todos os preços e retornar o valor dele
def calcular_total():
    total = 0
    for preco in precos:
        total += preco
    return total

## função para pegar o total e adicionar o desconto nele
def calcular_total_com_desconto():
    total = calcular_total()
    desconto = calcular_desconto()
    desconto_total = total - desconto
    return desconto_total, desconto

## esta função é outra um pouco mais complexa, mas ela faz o calculo do troco e ainda diz quantas notas e moedas precisa devolver
def calcular_troco(dinheiro_pago):
    desconto_total, _ = calcular_total_com_desconto()
    ## exibindo o quanto precisa ser devolvido
    print("______________________________\n")
    print(f"Total a pagar: R${desconto_total:.2f}")
    print(f"Total pago: R${dinheiro_pago:.2f}")
    print("______________________________\n")
    troco = dinheiro_pago - desconto_total
    valor = int(round(troco * 100)) 
    print(f"Troco: R${valor / 100}")
    print("==============================")

    notas = [10000, 5000, 2000, 1000, 500, 200]
    moedas = [100, 50, 25, 10, 5, 1]
    ## fazendo a contagem das notas
    print("Notas:")
    for nota in notas:
        qtd = valor // nota
        if qtd > 0:
            print(f"{qtd} nota(s) de R${nota / 100:.2f}")
        valor %= nota
    print("==============================")
    ## fazendo a contagem das moedas
    print("Moedas:")
    for moeda in moedas:
        qtd = valor // moeda
        if qtd > 0:
            print(f"{qtd} moeda(s) de R${moeda / 100:.2f}")
        valor %= moeda
    print("==============================")
    input("Entregue o troco restante e tecle qualquer tecla para finalizar.")

    
## função que mostra as listas e o valor total junto com o desconto
def mostrar_lista():
    for produto, quantidade, preco in zip(produtos, quantidades, precos):
        print(f"{produto} [{quantidade} unidade(s)]: R$ {preco:.2f}")

    desconto_total, desconto = calcular_total_com_desconto()

    print("______________________________")
    print(f"Desconto: R${desconto:.2f}")
    print(f"\nTotal: R${desconto_total:.2f}")
    print("______________________________")
    mostrar_opcoes()

## função que exibe as opções com outras funções
def mostrar_opcoes():
    print("Digite o número para selecionar a lista ordenada abaixo:")
    print("1. Adicionar cupom de desconto")
    print("2. Adicionar mais um item à lista")
    print("3. Remover item da lista")
    print("4. Cancelar a compra.\n")
    resposta = input("Ou Digite qualquer tecla para fazer o pagamento.\n")

    match resposta:
        case '1':
            adicionar_cupom()
        case '2':
            registrar_mercadorias()
        case '3':
            remover_lista()
        case '4':
            print("Compra cancelada.")
            pass
        case _:
            metodo_de_pagamento()

## função para adicionar o cupom de desconto a compra
def adicionar_cupom():
    cupom = input("Adicione o seu cupom:\n")
    total = sum(precos)

    ## o cupom só poderá ser usado se ele não tiver sido usado e ativado
    if cupom in cupons_disponiveis and cupom not in cupons_ativados:
        desconto = cupons_disponiveis[cupom]
        ## caso o cupom exceder o valor do produto, ele não poderá ser usado
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