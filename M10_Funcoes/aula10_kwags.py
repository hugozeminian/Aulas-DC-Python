# Argumento Arbitrário **Kwargs - Keyword Arguments
# Essa função recebe argumentos que serão atribuídos em um dicionário

# é utilizado quando não sabemos quantos argumentos nomeados serão passados para a função

def imprimir_nomes(**nomes):
    print(f'{nomes['nome']}'{nomes['sobrenome']})


imprimir_nomes(nomes='ana', sobrenome='julia')
