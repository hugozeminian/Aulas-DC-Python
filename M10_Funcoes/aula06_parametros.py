# Parâmetros de uma função

# parâmetro é o nome dado ao valores utilizados na definição de uma função
'''
exemplo1

def nome_da_funcao(parametro):
    # corpo da função
    print('ola', parametro)


nome = input('Qual o seu nome? ')
# argumento é o nome dado aos valores utilizados na chamada de uma função
nome_da_funcao(nome)
'''

'''exemplo 2'''


def imprime_nome(nome):  # temos que passar a quantidade exata de argumentos para dentro da função, se passar menos ou mais irá gerar um erro
    print('olá,', nome)


nome = input('Qual o seu nome? ')
imprime_nome(nome)
