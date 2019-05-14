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

    escolha = input('>>> ')

    return escolha

def menuFuncionario():
    print('1. Ver estoque')
    print('2. Cadastrar item')
    print('3. Remover item')
    print('4. Atualizar item')
    print('5. Buscar usuario')
    print('6. Atualizar usuario')
    print('7. Verificar compras/transacoes realizadas')
    print('0. Sair')

    escolha = input('>>> ')
    return escolha

def menuGerente():
    print('1. Ver estoque')
    print('2. Cadastrar item')
    print('3. Remover item')
    print('4. Atualizar item')
    print('5. Buscar usuario')
    print('6. Atualizar usuario')
    print('7. Alterar perfil de usuario')
    print('8. Quantidade de usuarios cadastrados')
    print('9. Verificar compras/transacoes realizadas')
    print('0. Sair')

    escolha = input('>>> ')
    return escolha

def systemGerente(option):
    if option == '1':
        visualizarLivros()
    elif option == '2':
        cadastroLivro()
    elif option =='3':
        removeLivro()
    elif option == '4':
        atualizaLivro()
    elif option == '5':
        #buscarUsuario()
        pass
    elif option == '6':
        atualizaUsuario()
    elif option == '7':
        alteraPerfil()
        pass
    elif option == '8':
        print(f'Numero de usuarios cadastrados: {totalDeUsuarios()}\n')
    elif option == '9':
        #verificaCompra()
        pass
    else:
        return


def systemFuncionario(option):
    if option == '1':
        visualizarLivros()
    elif option == '2':
        cadastroLivro()
    elif option =='3':
        removeLivro()
    elif option == '4':
        atualizaLivro()
    elif option == '5':
        #buscarUsuario()
        pass
    elif option == '6':
        atualizaUsuario()
    elif option == '7':
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
            choice = menuGerente()
            systemGerente(choice)

        elif perfil == 'funcionario':
            choice = menuFuncionario()
            systemFuncionario(choice)

        elif perfil == 'cliente':
            choice = menuCliente()
            systemCliente(choice)

        if choice == '0':
            on = False


# Acoes que envolvem o baco de dados (dataBase.txt)
def totalDeUsuarios():
    with open('dataBase.txt','r') as base:
        total = len(base.readlines())

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

def alteraPerfil():
    len = totalDeUsuarios()
    id = input('Deseja alterar o perfil de qual usuario (ID)?\n>>> ')
    new_perfil = input('Qual o novo perfil ?\n>>> ')

    with open('database.txt', 'r') as base:
        pessoas = base.readlines()

    with open('database.txt', 'r') as base:
        for x in range(len):
            usuario = base.readline().split(',')

            if usuario[Pessoa.id.value] == id:
                usuario[Pessoa.perfil.value] = new_perfil
                break

    pessoas.pop(x)
    pessoas.insert(x,','.join(usuario))
    with open('database.txt', 'w') as base:
        base.writelines(pessoas)
    print('Perfil alterado com sucesso\n')

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

    novoLivroString = ','.join(novoLivro)
    livros.write(novoLivroString)
    livros.close()

def buscaLivro():
    book_search = input('\nQual livro esta procurando ?\n>>> ')
    livros = open('livros.txt','r')
    livro_list = []
    book_index = -1
    book_not_found = 0

    while livro_list != ['']:

        livro_list = livros.readline().strip(',\n').split(',')
        book_index += 1

        try:
            if livro_list[Livro.obra.value] == book_search:
                livro_list = []
                break
        except IndexError:
            livro_list = ['']

    livros.close()
    return book_index if livro_list == [] else book_not_found

def removeLivro():
    index = buscaLivro()

    with open('livros.txt', 'r') as livro:
        book = livro.readlines()

    with open('livros.txt','w') as livro:
        if index:
            book.pop(index)
            livro.writelines(book)
            print('Removido com sucesso\n')
        else:
            livro.writelines(book)
            print('Livro nao encontrado\n')


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