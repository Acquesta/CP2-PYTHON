ano = input("Digite seu ano de nascimento: ")

vinhoB = 10
vinhoM = 40
vinhoC = 70

totalVinhos = 0

qtdB = 0
qtdM = 0
qtdC = 0

while not ano.isnumeric():
    ano = input('Seu ano precisa ser um número: ')

ano = int(ano)

if ano <= 2006:
    endereco = input('Digite seu endereço: ')

    while True:

        vinho = input('Escolha sua opção de vinho: \n'
                       '1 - Vinho caro (R$ 70)\n'
                       '2 - Vinho médio (R$ 40)\n'
                       '3 - Vinho barato (R$ 10) \n'
                           'Digite sua opção: ')

        if not vinho.isnumeric() or vinho != '1' and vinho != '2' and vinho != '3':
            print("Você precisa digitar uma das opções")
            continue

        qtd = input("Digite a quantidade dele: ")

        while not qtd.isnumeric():
            qtd = input("A quantidade precisa ser um número: \n"
                        "Digite novamente: ")

        qtd = int(qtd)

        if vinho == '1':
            qtdC += qtd
            totalVinhos += vinhoC * qtdC
        elif vinho == '2':
            qtdM += qtd
            totalVinhos += vinhoM * qtdM
        else:
            qtdB += qtd
            totalVinhos += vinhoB * qtdB

        comprarDnv = input("Você quer fazer mais uma compra ? \n"
                           "1 - s \n"
                           "2 - n \n"
                           ":")
        while comprarDnv != 's' and comprarDnv != 'n':
            comprarDnv = input('O valor precisa ser "s" ou "n" !!!\n'
                               'Digite novamente: ')

        if comprarDnv == 's':
            continue

        break

    if totalVinhos > 500:
        totalVinhos += 10

    print(f"Sua compra total foi de {totalVinhos} \n"
          f"Você comprou {qtdB} dos vinhos baratos \n"
          f"Você comprou {qtdM} dos vinhos médios \n"
          f"Você comprou {qtdC} dos vinhos caros \n")
    print('Obrigado por comprar na nossa loja !!!! \n'
          f'Entregaremos na {endereco}, o seu pedido')
else:
    print("Voce precisa ser maior de idade")

