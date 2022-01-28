'''
Exercícios - Python

Observação: Todos os exercícios devem utilizar a função input, de forma que o usuário possa determinar os dados de entreda.

01 - área de um retângulo
02 - área de um quadrado
03 - 
04 - Se o produto que você quer avalair custa (??) reais, qual será o valor do mesmo com desconto de (??)%
05 - área de um círculo
06 - conversão de reais para dolar
07 - conversão de dolar para reais
'''

import math
print('01 - área de um retângulo')
larguraRet = int(input('Qual a largura? '))
alturaRet = int(input('Qual a altura? '))
areaRet = alturaRet * larguraRet
print(f'A área do retângulo é: {areaRet}.')

print('02 - área de um quadrado')
larguraQd = int(input('Qual a largura? '))
areaQd = larguraQd * larguraQd
print(f'A área do retângulo é: {areaQd}.')


print('04 - Se o produto que você quer avalair custa (??) reais, qual será o valor do mesmo com desconto de (??)%')
precoProd = float(input('Qual o valor do produto? '))
desconto = float(input('Qual o valor do desconto em % ? '))
ProdDesc = precoProd - (precoProd * desconto / 100)
print(ProdDesc)
print(
    f'O valor do produto é {precoProd} reais e possui desconto de {desconto}%, portanto o valor final dele é: {ProdDesc} reais.')

print('05 - área de um círculo')
raio = int(input('Qual o raio do circulo? '))
areaCirc = math.pi * math.pow(raio, 2)
print(areaCirc)


print('06 - conversão de reais para dolar')
reais = float(input('Quantos reais deseja converter para dolares? '))
dolar = 5
conv = reais / dolar
print(f'O valor de {reais} reais são {conv} dolares')

print('07 - conversão de dolar para reais')
dolar2 = float(input('Quantos dolares deseja converter para reais? '))
reais2 = 5
conv2 = reais2 * dolar2
print(f'O valor de {dolar2} reais são {conv2} dolares')
