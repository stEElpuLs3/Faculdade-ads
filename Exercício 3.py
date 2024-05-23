def escolha_servico(): #funçao para escolher o serviço
    print('Bem vindo a Papelaria do Vitor.')
    while True:
        servico = input('\n'
                        'Escolha o serviço desejado: \n'
                        'DIG - Digitalização \n'
                        'ICO - Impressão colorida \n'
                        'IBO - Impressão preto e branco \n'
                        'FOT - Fotocopia \n'
                        '\n'
                        'Digite uma opção de serviço:').upper()
        if servico in ['DIG', 'ICO', 'IBO', 'FOT']:
            return servico
        else:
            print('Opção de serviço inválida, tente novamente.')

def servico_extra(): #calcular o serviço extra, retorna 0 caso n tenha
    valor_extra = 0
    while True:
        servico_extra = int(input('Gostaria de algum servico extra? \n'
                             '1 - Encadernação Simples R$ 15,00\n'
                             '2 - Encadernação Capa Dura R$ 40,00\n'
                             '0 - Nao desejo mais nada\n'))
        if servico_extra == 1:
            valor_extra += 15
        elif servico_extra == 2:
            valor_extra += 40
        elif servico_extra == 0:
            return valor_extra
            print('Saindo...')
        else:
            print('opçao invalida, tente novamente.')


def num_pagina(): #função para calcular o desconto com base no numero de paginas

    while True:
        try:
            num_paginas = int(input('Insira o numero de copias:'))
            if num_paginas <= 20:
                return num_paginas  # sem nenhum desconto

            elif 20 <= num_paginas < 200:
                return num_paginas * 0.85

            elif 200 <= num_paginas < 2000:
                return num_paginas * 0.80

            elif 2000 <= num_paginas < 20000:
                return num_paginas * 0.75

            else:
                print('Numero de paginas nao permitido, tente novamente.')
        except ValueError:
            print('Por favor, utilize numeros.')

def mostrar_resumo(servico, num_paginas, valor_extra): # função para ver o resumo do pedido
    preco_servico = {"DIG": 1.10, "ICO": 1.00, "IBO": 0.40, "FOT": 0.20}
    print('-' * 50)
    print('Resumo do pedido:')
    print(f'Serviço escolhido: {servico}')
    print(f'Numero de paginas escolhidas: {num_paginas}')
    print(f'Servico extra: R${valor_extra},00')
    print(f'Total do pedido: R${preco_servico[servico] * num_paginas + valor_extra}')

#O programa principal
def main():
    try:

        servico = escolha_servico()
        num_paginas = num_pagina()
        valor_extra = servico_extra()
        preco_servico = {"DIG": 1.10, "ICO": 1.00, "IBO": 0.40, "FOT": 0.20}
        total = preco_servico[servico] * num_paginas + valor_extra
        print(f'Total a pagar: R${total}0')
        mostrar_resumo(servico, num_paginas, valor_extra)
    except KeyboardInterrupt:
        print('Encerrando...')
    except Exception as e:
        print(f'Erro: {e}')

if __name__ == '__main__':
    main()


