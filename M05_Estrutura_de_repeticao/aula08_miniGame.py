'''
do while

Código para adivinhar um número

**No geral para Python, variáveis, funções, classes, objetos vazios são considerados como falsos.
Para números, se for zero ou vazio, python também reconhece como falso.

'''

palpite = 9
numero = 9

# o While não possui limite como o FOR, mas sim depende de uma condição
while palpite != numero:
    print('Qual o numero correto?')
    palpite = int(input())
    
print('Parabens voce acertou')
# print('Voce errou')

print(bool(3>8))
print(bool(palpite))