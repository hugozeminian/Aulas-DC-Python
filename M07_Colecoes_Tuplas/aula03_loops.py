tupla = ('item1',)
tupla2 = ('a', 'b')

tupla = 'item1', 'item2', 'item3', 'item4', 'item5'
print(tupla)

for x in tupla:
    print(x)

for x in range(len(tupla)):
    print(x, tupla[x])

# Atribuir valores a uma lista (empacotar) - serve para lista ou tupla

# Desempacotar uma tupla
print('### desempacotar uma tupla ###')
'''
(x, y, z) = tupla
print(x)
print(y)
print(z)
'''

print()
# outro método, caso queira passar apenas um valor para a variável (no exemplo o primeiro e o ultimo, ficado o restante como lista)
(x, *y, z) = tupla
print(x)
print(y)
print(z)
