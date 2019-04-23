def menu():
    print('1. Login')
    print('2. Cadastro')
    escolha = int(input('Escolha: '))
    return escolha


def verifica(id,senha):
    pessoas = open('dataBase.txt', 'r')
    listPessoa = pessoas.read().split(',')

    if listPessoa[0] == id and listPessoa[1] == senha:
        print('Ola, ' +id[:])
    else:
        print('Usuario ou senha invalidos')
    pessoas.close()

escolha = menu()
if escolha == 1:
    id = input('id: ')
    senha = input('senha: ')
    verifica(id,senha)
elif escolha == 2:
    print('Not yet implemented')

