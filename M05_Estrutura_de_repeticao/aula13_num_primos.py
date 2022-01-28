'''
Descobrir se um numero é primo

'''

print(30 * '-')

numero = int(input("Insira um numero para descobrir se ele é primo "))

if numero > 1:
    for x in range(1, numero):
        if(numero % x) == 0:
            print('Esse não é um número primo')
            break
        else:
            print('Esse número é primo')
else:
    print('Esse número não é primo, número menor ou igual a 1')

    print(30 * '-')
