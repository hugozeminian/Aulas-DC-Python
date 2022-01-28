lista = [1, 2, 3, 4, 5]
print(lista)

# retorna a variável que foi eliminada e armazena o valor na variavel var1
retorno = lista.pop()
var1 = print('olá mundo')  # retorno none, ou seja, não possui retorno
print(lista)
print("Retorno da função pop: ", retorno)
print("Retorno da função print: ", var1)

print(30 * '-')


def ola_mundo():
    return 'ola mundo'


'''
retorno = ola_mundo()
print(retorno)
abaixo uma forma de escrita que mantém o código mais limpo'''
print(ola_mundo())

# não é possível ter uma função com o corpo vazio, isso gera um erro. Porém caso vc bypass esse erro, é possível escrever no corpo da função a palavra pass e este erro será ignorado. O mesmo se aplica para o if.
''' exemplo
def par_impar():
    pass
'''

print(30 * '-')


def par_impar():
    numero = 4
    if (numero % 2) == 0:
        return 'numero par'
    return 'numero ímpar'
    # ao utilizar a palavra return, saimos automáticamente do código


print(par_impar())

x = 0
if x == 0:
    print('0')
print('olá')
