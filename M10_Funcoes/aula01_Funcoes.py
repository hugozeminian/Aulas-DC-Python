# Paradigma imperativo ou tipos de programação

# Características de um programa paradigma:
# variáveis, atribuições e principalmente sequêncial.

# exemplos de programas que utilizam a linguagem imperativo: C, Fortran, Cobol, Basic, Pascal, Ada, Modula-2

# variável global - acessível em todo bloco
# variável interna - acessível apenas dentro do seu escopo
# toda função em Python, se inicia com def nome


# bloco externo
nome = 'Gabriel'  # variável global


def minha_funcao():
    # bloco interno *bloco interno de uma função é conhecido como corpo da função
    nome = "Ana"  # variável local
    tupla = 2, 5, 6, 7, 9
    print(nome)
    print(tupla)
    if nome == 'Ana':
        print('Impressão do bloco interno da condição if')
    for x in tupla:
        print(x)
    # ao terminar a função é necessário sempre pular duas linhas para garantir que não haja nenhum erro


print(nome)
minha_funcao()
