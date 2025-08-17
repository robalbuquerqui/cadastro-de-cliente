#Este é um sistema de cadastro de clientes simples e funcional que estou desenvolvendo.
#Colocando em prática com base no que estou apredendo.

def menu():
    print('\n===CADASTRO DE CLIENTES===')
    print('1 - Cadastrar Cliente')
    print('2 - Listar Clientes')
    print('3 - Editar Cliente')
    print('4 - Remover Cliente')
    print('5 - Sair')


lista_clientes = []


def cadastro():
    nome = input('Nome: ')
    cpf = int(input('CPF: '))
    email = input('Email: ')
    telefone = int(input('Telefone: '))
    clientes = {'nome': nome, 'cpf': cpf, 'email': email, 'telefone': telefone}
    lista_clientes.append(clientes)
    print('Cliente cadastrado com sucesso!')
    return lista_clientes



while True:
    menu()
    opcao = input('Escolha uma opcao: ')

    if opcao == '1':
       cadastro()

    elif opcao == '2':
        for clientes in lista_clientes:
            print(clientes)

    elif opcao == '3':
        if not lista_clientes:
            print('Nenhum cliente cadastrado')
        else:
            for i, cliente in enumerate(lista_clientes):
                print(i, cliente)
            ind = int(input('Qual cliente você deseja editar? Digite o número: '))
            if 0 <= ind < len(lista_clientes):
                nome = input('Novo Nome: ')
                cpf = int(input('Novo CPF: '))
                email = input('Novo Email: ')
                telefone = int(input('Novo Telefone: '))
                lista_clientes[ind] = {'nome': nome, 'cpf': cpf, 'email': email, 'telefone': telefone}
                print('Cliente editado com sucesso!')
            else:
                print('Opção inválida!')

    elif opcao == '4':
        if not lista_clientes:
            print('Nenhum cliente cadastrado')
        else:
            for i, cliente in enumerate(lista_clientes):
                print(i, cliente)
            ind = int(input('Qual cliente você deseja remover? Digite o número: '))
            if 0 <= ind < len(lista_clientes):
                del lista_clientes[ind]
                print('Cliente removido com sucesso!')
            else:
                print('Opção inválida!')

    elif opcao == '5':
        print('Saindo...')
        break

    else:
        print('Opção inválida!')

