print ('Seja bem vindo ao Mercado do Vitor')

valor = float(input('Qual o valor do produto? '))
qtd = int(input('Qual a quantidade de produtos? '))
final = valor * qtd
if final < 2500: # sem desconto abaixo desse valor
    print(f'Para o valor a pagar ({final}) nao existe desconto')
elif final >= 2500 and final < 6000:
    desconto = final * 0.04
    print(f'O valor total era {final} e agora é {final - desconto}')
elif final >= 6000 and final < 10000:
    desconto = final * 0.07
    print(f'O valor total era {final} e agora é {final - desconto}')
else: #todas as outras opçoes vao cair aqui.
    desconto = final * 0.11
    print(f'O valor total era {final} e agora é {final - desconto}')