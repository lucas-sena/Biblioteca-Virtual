from enum import Enum
# from datetime import datetime

class Pessoa(Enum):
    id = 0
    senha = 1
    nome = 2
    data = 3
    cpf = 4
    perfil = 5

class Livro(Enum):
    id = 0
    obra = 1
    autor = 2
    ano = 3
    tipo = 4

def menuLogin():
    print('1. Login')
    print('2. Cadastro')
    escolha = input('>>> ')
    return escolha

def hierarquia(perfil):
    if perfil == 'adm':
        #tudo
        pass
    elif perfil == 'funcionario':
        cadastroLivro()
        #atualizaLivro
        #verificaLivro
        #atualizaUsuario
        pass
    elif perfil == 'cliente':
        #comprar, assinar, etc.
        pass
    else:
        #mostrar informacoes de pendencia
        pass


def totalDeUsuarios():
    base = open('dataBase.txt','r')
    total = len(base.readlines())
    base.close()

    return total


def verificaLogin(id, senha):
    total = totalDeUsuarios()
    base = open('dataBase.txt', 'r')

    for x in range(total):
        usuario = base.readline().split(',')

        if usuario[Pessoa.id.value] == id and usuario[Pessoa.senha.value] == senha:
            print('Bem-vindo(a), ' + usuario[Pessoa.nome.value])
            base.close()
            return usuario[Pessoa.perfil.value]

    print('Usuario ou senha incorreto')

    base.close()


def cadastroUsuario():
    base = ['ID','Senha','Nome','Data de Nascimento','CPF']
    novaPessoa = []
    for x in range(len(base)):
        novaPessoa += [input('{}: '.format(base[x]))]

    novaPessoa.append('\n')
    if verificaLogin(novaPessoa):
        return

    pessoas = open('dataBase.txt', 'a')
    novaPessoaString = ','.join(novaPessoa)
    pessoas.write(novaPessoaString)
    pessoas.close()

    print('-- Cadastrado com sucesso --')


def atualizaUsuario():
    pass

def verificaLivro():
    pass

def numeroDeLivros():
    pass


def cadastroLivro():
    livros = open('livros.txt','r+')
    posicao = str(len(livros.readlines()) + 1)

    base = ['Obra', 'Autor', 'Ano', 'Tipo']
    novoLivro = []
    for x in range(len(base)):
        novoLivro += [input('{}: '.format(base[x]))]

    novoLivro.insert(0,posicao)
    novoLivro.append('\n')

    novoLivroString = ','.join(novoLivro)
    livros.write(novoLivroString)
    livros.close()

def atualizaLivro():
    pass

# main
escolha = menuLogin()

if escolha == '1':
    id = input('Id: ')
    senha = input('Senha: ')
    perfil = verificaLogin(id, senha)
    hierarquia(perfil)
elif escolha == '2':
    cadastroUsuario()
else:
    pass