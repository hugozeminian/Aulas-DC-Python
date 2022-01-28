'''
Como descobrir se um número é ímpar ou par

'''

numero = int(input('Digite um número: '))

print(30 * '-')
if (numero % 2) == 0:
    print(f'{numero} é um numero par')
else:
    print(f'{numero} é um numero impar')
print(30 * '-')