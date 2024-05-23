print('Bem vindo a Sorveteria do Vitor')
print('------------------ Cardapio -----------------')
print('---| Tamanho | Cupuaçu (CP) |  Açai (AC) |---')
print('---|    P    |   R$  9,00   |  R$ 11,00  |---')
print('---|    M    |   R$ 14,00   |  R$ 16,00  |---')
print('---|    G    |   R$ 18,00   |  R$ 20,00  |---')
print('---------------------------------------------')

total = 0  #acumulador
while True:  #esse loop vai permanecer indefinidamente ate o break ser chamado
    sabor = input('Qual o sabor? (AC/CP):')

    if sabor != 'AC' and sabor != 'CP':
        print('sabor nao existe, tente novamente')
        continue  #preso na pergunta ate responder corretamente
    elif sabor == 'AC':
        tamanho = input('Qual o tamanho? (P/M/G):')
        while tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
            print('Tamanho errado, tente novamente')
            tamanho = input('Qual o tamanho? (P/M/G):')

        if tamanho == 'P':
            total += 11
            print(f'um ACAI Pequeno de R$ 11,00 reais, o total da sua compra ate agora é de R$ {total},00')
        elif tamanho == 'M':
            total += 16
            print(f'um ACAI Medio de R$ 16,00 reais, o total da sua compra ate agora é de R$ {total},00')
        else:
            total = total + 20
            print(f'um ACAI Grande de R$ 20,00 reais, o total da sua compra ate agora é de R$ {total},00')

    elif sabor == 'CP':
        tamanho = input('Qual o tamanho? (P/M/G):')
        while tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
            print('Tamanho errado, tente novamente')
            tamanho = input('Qual o tamanho? (P/M/G):')

        if tamanho == 'P':
            total += 9
            print(f'um CUPUACU Pequeno de R$ 9,00 reais, o total da sua compra ate agora é de R$ {total},00')
        elif tamanho == 'M':
            total += 14
            print(f'um CUPUACU Medio de R$ 14,00 reais, o total da sua compra ate agora é de R$ {total},00')
        else:
            total += 18
            print(f'um CUPUACU Grande de R$ 18,00 reais, o total da sua compra ate agora é de R$ {total},00')

    sair = input('Quer continuar? (S/N):') #Após cada pedido essa pergunta é feita
    while sair != 'S' and sair != 'N':
        sair = input('Quer continuar? (S/N):')
    if sair == 'S':
        continue
    else:
        print(f'o total da sua compra foi de R${total},00.') #Finaliza aqui com o valor total
        print('Por favor, dirija-se ao caixa, e volte sempre!')
        break
