# 01 - Escreva um programa que leia 5 valores e encontre o maior e o menor deles. Mostre o resultado.

num = []
for i in range(1, 6):
    numeroInput = int(input(f'{i} - Digite um número: '))
    num.append(numeroInput)

print(f'Números digitados: {num}')

num.sort()
print(f'O menor número digitado foi: {num[0]}')

num.reverse()
print(f'O maior número digitado foi: {num[0]}')


# refatorando o código para apresentar o maior e menor valor da lista 
num = []
for i in range(1, 6):
    numeroInput = int(input(f'{i} - Digite um número: '))
    num.append(numeroInput)
print(f'Números digitados: {num}')
print(f'O menor número digitado foi: {max(num)}')
print(f'O maior número digitado foi: {min(num)}')