'''
01 - Escreva um programa em que sejam lidos dois números reais, X e Y, e sejam feitas
chamadas a funções descritas abaixo, que deverão ser implementadas. No escopo global
deve ser impresso o resultado retornado por estas funções.
a) Uma função que receba X e Y como entrada e retorne o maior deles;
b) Uma função que receba X e Y como entrada e retorne a média aritmética deles;
'''

print('Exercício 1')
# variaveis globais
n = []


# funções


def maior_numero(max_n):
    print(f'O maior número digitado foi: {max_n}')


def media_aritmetica(n1, n2):
    print(f'A média aritmética de {n1} e {n2} é: {(n1+n2)/2}')


# main
for i in range(1, 3):
    while True:
        try:
            numero = float(input(f'{i}- Digite um número real: '))
            if(type(numero) == float):
                n.append(numero)
                break
        except ValueError:
            print('Entrada invalida, insira um número.')


for i in range(1, 3):
    print(f'O {i}° número digitado foi: {n}')


maior_numero(max(n))
media_aritmetica(n[0], n[1])


'''
02 - Escreva uma função de potenciação, em que os dados de entrada são: 
base e expoente (inteiros).
'''
print(30 * '-')
print('Exercício 2 - base e expoente')

# variaveis globais
base = None
exp = None


# funções


def input_base():
    while True:
        try:
            base = int(input(f'Digite um número inteiro para base: '))
            if(type(base) == int):
                return base
                break
                print('Entrada invalida, insira um número inteiro.')
        except ValueError:
            print('Erro - Entrada invalida, insira um número inteiro.')


def input_exp():
    while True:
        try:
            exp = int(input(f'Digite um número inteiro para expoente: '))
            if(type(exp) == int):
                return exp
                break
            else:
                print('Entrada invalida, insira um número inteiro.')
        except ValueError:
            print('Erro - Entrada invalida, insira um número inteiro.')


def potenciacao(base, exp):
    print(f'O valor da potenciação é: {base ** exp}')


# main
base = input_base()
exp = input_exp()
print(f'Valor da base: {base}')
print(f'Valor do expoente: {exp}')
potenciacao(base, exp)


'''
03 - Crie uma calculadora que consiga executar as funções destacadas da calculadora
padrão do windows 10.
'''