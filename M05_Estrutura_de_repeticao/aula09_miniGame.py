'''
do while

Código para adivinhar um número

**No geral para Python, variáveis, funções, classes, objetos vazios são considerados como falsos.
Para números, se for zero ou vazio, python também reconhece como falso.**

'''

palpite = 5
numero = 9

while bool(palpite) is True:
    print('Qual o numero correto?')
    palpite = int(input())
    if palpite == numero:
        print('Parabens voce acertou')
        break
    else:
        print('Voce errou')

print(bool(palpite))