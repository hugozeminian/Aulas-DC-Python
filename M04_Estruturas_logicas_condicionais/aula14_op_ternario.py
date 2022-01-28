'''
Operador Ternário

Uma conforma de reduzir a escrita do IF

'''

a = 8
b = 5
c = 2

if b > a:
    print('b é maior que a')
print('código fora do bloco if')

# operador ternário ou expressões condicionais
print('B') if b > a else print("A")

# alinhamento de if

if a > b:
    if a > c:
        print("A é maior que B e do que C")
