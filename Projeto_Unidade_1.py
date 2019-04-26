from enum import Enum


class Dados(Enum):
    id = 0
    senha = 1
    nome = 2
    data = 3
    cpf = 4


def menu():
    print('1. Login')
    print('2. Cadastro')
    escolha = int(input('Escolha: '))
    return escolha


def totalDeUsuarios():
    base = open('dataBase.txt','r')
    total = len(base.readlines())
    base.close()

    return total


def verifica(id, senha):
    total = totalDeUsuarios()
    base = open('dataBase.txt', 'r')
    flag = 1

    for x in range(total):
        usuario = base.readline().split(',')

        if usuario[Dados.id.value] == id and usuario[Dados.senha.value] == senha:
            print('Bem vindo, ' + usuario[Dados.nome.value])
            return

    print('Usuario ou senha incorreto')

    base.close()


def cadastro():
    pessoas = open('dataBase.txt','a')

    base = ['Id','Senha','Nome','Data de Nascimento','CPF']
    novaPessoa = []
    for x in range(5):
        novaPessoa += [input('{}: '.format(base[x]))]

    novaPessoaString = ','.join(novaPessoa)
    pessoas.write(novaPessoaString)
    pessoas.close()

escolha = menu()
if escolha == 1:
    id = input('Id: ')
    senha = input('Senha: ')
    verifica(id, senha)
elif escolha == 2:
    cadastro()
