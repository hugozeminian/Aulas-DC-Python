'''
Como achar o fatorial de um número

-> 4! = 4*3*2*1
'''

numero = int(input('Insira um número: '))

fatorial = 1

if numero < 0:
    print('Não existe fatorial de números negativos')
elif numero == 0:
    print(f'O fatorial de {numero} é: 1')
else:
    for i in range(1, numero+1):
        fatorial = fatorial * i
        
print(f'O fatorial de {numero} é: {fatorial}')