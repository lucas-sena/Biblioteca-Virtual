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


def verifica(id, senha):
    pessoas = open('dataBase.txt', 'r')
    listPessoa = pessoas.read().split(',')

    if listPessoa[Dados.id.value] == id and listPessoa[Dados.senha.value] == senha:
        print('Bem vindo, ' + listPessoa[Dados.nome.value])
    else:
        print('Usuario ou senha invalidos')
    pessoas.close()


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
