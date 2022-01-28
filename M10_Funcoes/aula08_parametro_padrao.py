# Parâmetro padrão --> Define argumentos não obrigatórios


# Dessa maneira os parâmetros se tornam opcionais. Obs.: Primeiramente sempre deve ser declarado os parâmetros obrigatórios e posteriormente os parâmetros opcionais dentro de uma função. Caso contrário irá gerar erro.
'''
def imprimir_nome(nome=None, sobrenome=None, idade=None):
    if nome != None:
        print(f'nome: {nome}')
        print(f'sobrenome: {sobrenome}')
        print(f'idade: {idade}')
        print(30 * '-')
    else:
        print('Por favor insira seus dados')
        print(30 * '-')


imprimir_nome()
imprimir_nome('hugo', 'zamian', 33)
'''

# Exemplos de números de argumentos com <= números dos parâmetros


def imprimir_imovel(nomeImovel, n_quartos, vagasGaragem=None):
    print(30 * '-')
    print('Título: ', nomeImovel)
    print('Quartos: ', n_quartos)
    if vagasGaragem != None:
        print('Vagas na garagem: ', vagasGaragem)


print()
imprimir_imovel('Casa 3 quartos - SP', 3)
imprimir_imovel('Apartamento - MG', 2, 1)

# Exemplos de números de argumentos com > números dos parâmetros ---> irá gerar um erro, na outra aula, mostra como é possível utilizar mais argumentos com *args
# imprimir_imovel('Apartamento - MG', 2, 1, 10, 5)
