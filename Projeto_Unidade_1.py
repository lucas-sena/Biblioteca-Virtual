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
    preco = 5

# Menu para cada tipo de perfil
def menuLogin():
    print('1. Login')
    print('2. Cadastro')
    escolha = input('>>> ')
    return escolha


def menuCliente():
    print('1. Ver livros disponiveis')
    print('2. Realizar compra')
    print('3. Alugar um livro')
    print('4. Tornar-se assinante')
    print('0. Sair')

    escolha = input('\n>>> ')

    return escolha

def menuFuncionario():
    print('1. Ver estoque')
    print('2. Cadastrar item')
    print('3. Remover item')
    print('4. Atualizar item')
    print('5. Buscar item')
    print('6. Buscar usuario')
    print('7. Atualizar usuario')
    print('8. Verificar compras/transacoes realizadas')
    print('0. Sair')

    escolha = input('\n>>> ')
    return escolha

def systemFuncionario(option):
    if option == '1':
        visualizarLivros()
    elif option == '2':
        cadastroLivro()
    elif option =='3':
        #removerLivro()
        pass
    elif option == '4':
        atualizaLivro()
    elif option == '5':
        #buscarLivro()
        pass
    elif option == '6':
        #buscarUsuario()
        pass
    elif option == '7':
        atualizaUsuario()
    elif option == '8':
        #verificaCompra()
        pass
    else:
        return

def systemCliente(option):
    if option == '1':
        visualizarLivros()
    elif option == '2':
        pass
    elif option == '3':
        pass
    elif option == '4':
        pass
    else:
        return


def hierarquia(perfil):
    on = True

    print('O que deseja ?')
    while on:
        if perfil == 'adm':
            pass

        elif perfil == 'funcionario':
            escolha = menuFuncionario()
            systemFuncionario(escolha)
            if escolha == '0':
                on = False
        elif perfil == 'cliente':
            escolha = menuCliente()
            systemCliente(escolha)

        else:
            #mostrar informacoes de pendencia
            pass


# Acoes que envolvem o baco de dados (dataBase.txt)
def totalDeUsuarios():
    base = open('dataBase.txt','r')
    total = len(base.readlines())
    base.close()

    return total


def verificaLogin(id, senha, flag=True):
    total = totalDeUsuarios()
    base = open('dataBase.txt', 'r')

    for x in range(total):
        usuario = base.readline().split(',')

        if usuario[Pessoa.id.value] == id and usuario[Pessoa.senha.value] == senha:
            print('Bem-vindo(a), ' + usuario[Pessoa.nome.value])
            base.close()
            return usuario[Pessoa.perfil.value]

    if not flag:
        print('Usuario ou senha incorreto')

    base.close()


def cadastroUsuario():
    base = ['ID','Senha','Nome','Data de Nascimento','CPF']
    novaPessoa = []
    for x in range(len(base)):
        novaPessoa += [input('{}: '.format(base[x]))]


    if verificaLogin(novaPessoa[Pessoa.id.value], novaPessoa[Pessoa.senha.value]):
        return

    novaPessoa.extend(('perfil pendente','\n'))

    pessoas = open('dataBase.txt', 'a')
    novaPessoaString = ','.join(novaPessoa)
    pessoas.write(novaPessoaString)
    pessoas.close()

    print('-- Cadastrado com sucesso --')


def atualizaUsuario():
    pass

# Acoes que envolvem o banco de dados (livro.txt)
def visualizarLivros():
    livros = open('livros.txt','r')
    flag = True

    print('\nESTOQUE:')
    while flag:
        book = livros.readline().strip(',\n')
        if not book:
            flag = False
        else:
            print(book)
    print('\n')
    livros.close()

def numeroDeLivros():
    pass


def cadastroLivro():
    livros = open('livros.txt','r+')
    posicao = str(len(livros.readlines()) + 1)

    base = ['Obra', 'Autor', 'Ano', 'Tipo', 'Preco']
    novoLivro = []
    for x in range(len(base)):
        novoLivro += [input('{}: '.format(base[x]))]

    novoLivro.insert(0,posicao)
    novoLivro.append('\n')

    novoLivroString = ', '.join(novoLivro)
    livros.write(novoLivroString)
    livros.close()

def buscaLivro():

    pass

def removeLivro():
    pass

def atualizaLivro():
    pass

# Main
escolha = menuLogin()

if escolha == '1':
    id = input('Id: ')
    senha = input('Senha: ')
    perfil = verificaLogin(id, senha, False)
    hierarquia(perfil)
elif escolha == '2':
    cadastroUsuario()
else:
    pass