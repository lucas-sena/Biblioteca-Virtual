# Biblioteca-Virtual
Primeiro projeto da disciplina LPAA.

## Contexto Geral
* O projeto de ser uma modelagem de um negócio/estabelecimento/empresa do mundo real ou
fictício de forma que seja possível realizar operações de gerenciamento sobre seus recursos. Ex:
Farmácias, Bibliotecas, empresas de modo geral.
* O sistema deve respeitar hierarquia de cargos. Ou seja, um cliente tem menos privilégios do que
um funcionário por exemplo. Portanto as opções que cada usuário pode acessar no sistema serão
restritas por perfil.
* Todas as operações realizadas pelo sistema, devem ser gravadas em um arquivo de texto com
nome log_NOME_PROJETO.txt.
* A gravação dos eventos em texto deve obedecer o seguinte formato:
  * [HORA ATUAL] : USUARIO -&gt; AÇÃO

* Em todos os projetos devem conter uma instancia para PESSOAS. Cada pessoa terá um ID,
Login, Senha, Nome, Idade, CPF, data de nascimento e por último, perfil.
  * O perfil descriminará se a pessoa é um ‘Perfil pendente’,‘cliente’,’funcionário’ ou
‘gerente’

* Uma PESSOA inicial deve ser criada com o perfil de ‘gerente’
* Ao iniciar o sistema, deverá ser apresentada uma mensagem dando as seguintes opções:
  * Inserir login e senha
  * Realizar cadastro

* Para entrada de dados do usuário, deve ser utilizado o comando raw_input
  * Não deve ser dada a opção de perfil ao ser criado um perfil para um novo cadastro
* Por padrão, todos os novos inscritos são ‘Perfil pendente’
* O login e senha ao serem conferidos, apresentarão as opções do sistema.

1. Clientes: apenas acessam funcionalidades voltadas para compras, alugueis, etc.
2. Funcionários: podem acessar todas as opções de clientes, adicionando-se operações
específicas como por exemplo, verificar estoque, cadastrar item, deletar item, atualizar
item, busca por item, busca por usuário, cadastro, atualização de usuários. Verificar
compras/transações realizadas.
3. Gerente: todas as opções de funcionário, adicionando-se operações gerenciais, como,
alteração de perfil de usuário, número de vendas em um determinado período,
quantidade de usuários cadastrados, número de usuários de uma determinada faixa etária,
lista de usuários de uma determinada faixa etária, lista de compras/alugueis/transações
realizadas por um determinado usuário em um determinado período, compras/transações
feitas por pessoas de uma determinada faixa etária em determinado período de tempo.
Gerenciamento de todas as transações que ocorrem no sistema.

* Elaborar um relatório gerencial, contendo número de transações, médias,
gráficos, etc.



## Contexto Específico
* O contexto específico envolverá todas as operações inerentes de cada projeto.
* Ex: Locadora
    * Supondo uma locadora de filmes. Será necessário cadastrar os filmes e categorizar por
id,tipo, nome, ano
    * Cada ID é único mesmo tendo várias cópias do mesmo filme
    * Deve-se, portanto, criar uma estrutura capaz de armazenar todas as locações realizadas,
contendo informações do filme e do usuário que o locou.
    * Deve-se também, estipular a data de entrega, verificar usuários pendentes de entrega,
verificar itens devolvidos.
    * Portanto deve-se manter a coerência da base de dados, ou seja, se um usuário for deletado, primeiro deve ser verificado se esse usuário possui pendências com a locadora.
    
    
## Contexto técnico
* O projeto deve ser implementado utilizando linguagem python, empregando:
  * Slicing
  * Compreensão de listas
  * Funções
  * Expressões lambda
  * Tratamento de exceções
* Aplicar uma regressão a um conjunto de dados que será fornecido mediante definição do tema do
projeto.
