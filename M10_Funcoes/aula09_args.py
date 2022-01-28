# Argumento Arbitrário *args
# - é utilizado quando não sabemos a quantidade de parâmetros que a função irá receber
# - irá armazenar os valores em forma de tupla.

def imprimir_imovel(nomeImovel, n_quartos, vagasGaragem=None, *outros):
    print(30 * '-')
    print('Título: ', nomeImovel)
    print('Quartos: ', n_quartos)
    if vagasGaragem != None:
        print('Vagas na garagem: ', vagasGaragem)


imprimir_imovel('Apartamento - MG', 2, 1, 10, 5)


def imprimir_nome(*nomes):
    print(30 * '-')
    print(nomes)
    print(type(nomes))
    print(nomes[0])


# neste exemplo mostra que a tupla é desempacotada dentro do argumento
lista = ['ana', 'beatriz', 'pedro', 'joão']
imprimir_nome(*lista)
