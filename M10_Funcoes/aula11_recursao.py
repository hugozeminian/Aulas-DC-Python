'''
numeroInt = 5
def reduzirNumero(numeroInt):    
    while numeroInt > 0:
        print(numeroInt)
        numeroInt -= 1


reduzirNumero(7)
'''
'''
Algorítmo
1 - checar se o nosso número não é igual a 0
2 - se ele não for igual a 0, reduzir 1 unidade, 
portanto N - 1
'''

# observe o caminho de ida e de volta da recursividade


def reduzirNumero(numeroInt):
    print(f'print no inicio da função ----> {numeroInt}')
    if numeroInt > 0:
        # N - 1
        reduzirNumero(numeroInt - 1)
        print(f'print no final da função ----> {numeroInt}')


reduzirNumero(5)
