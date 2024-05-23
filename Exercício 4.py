print('Bem vindo a Livraria do VITOR')
id_global = 0
lista_livro = []

def cadastrar(id): #função para cadastrar livros
    nome = str(input('Nome do livro: '))
    autor = str(input('Autor do livro: '))
    editora = str(input('Editora do livro: '))

    livro = {
        'ID': id,
        'nome': nome,
        'autor': autor,
        'editora': editora
    }
    lista_livro.append(livro)


def consultar(): #funçao para consultar livros
    opcao = input('Escolha uma opção :\n'
                  '1 - Consultar por ID\n'
                  '2 - Consultar por Autor\n'
                  '3 - Consultar Todos\n'
                  '4 - Retornar\n')
    if opcao == '3':
        for livro in lista_livro:
            print(livro)
    elif opcao == '1':
        id = int(input('ID do livro: '))
        for livro in lista_livro:
            if livro['ID'] == id:
                print(livro)
                break
            else:
                print('Nenhum livro foi encontrado')
    elif opcao == '2':
        autor = input('Digite o nome do autor: ')
        for livro in lista_livro:
            if livro ['autor'] == autor:
                print(livro)
            else:
                print('Nenhum autor foi encontrado')
    elif opcao == '4':
        return
    else:
        print('opçaõ invalida')

def remover(): #função para remover livros
    id = int(input('ID do livro: '))
    for livro in lista_livro:
        if livro['ID'] == id:
            lista_livro.remove(livro)
            print('livro removido com sucesso')
            return
        else:
            print('Nenhum livro foi encontrado')


while True: #main code, inclusive deixei o id global incremetado aqui e nao na funçao de cadastrar
    print('Bem vindo ao Registro de Livros do Vitor\n'
          '1 - Cadastrar um Livro\n'
          '2 - Consultar um Livro\n'
          '3 - Remover um Livro\n'
          '4 - Sair\n')
    x = input('Escolha a opçao:\n')

    if x == '1':
        id_global = id_global + 1
        cadastrar(id_global)
        print('Livro cadastrado com sucesso!')
    elif x == '2':
        consultar()
    elif x == '3':
        remover()
    elif x == '4':
        print('Encerrando...')
        break
    else:
        print('opção invalida, escolha uma valida...')
