lista = ['a', 'b', 'c']
lista2 = [1, 4, 6]

# forma de concatenar listas
# 1
'''
lista = lista + lista2
print(lista)
'''

# 2
'''
lista.extend(lista2)
print(lista)
'''

# 3
'''
for x in lista2:
    lista.append(x)
print(lista)
'''

# como copiar uma lista para outra lista
# da forma abaixo ao adicionar um elemento na lista 1, ou na lista 2, ele também irá aparecer na outra lista
lista = ['a', 'b', 'c']
print(lista)

lista2 = lista
print(lista2)

lista2.append('d')
lista.append('e')
print(lista)
print(lista2)


# mesmo exemplo de cópia, porém utilizando a função copy()
# as listas ficaram independentes quando tiveram elementos adicionados
print('### função copy() ###')
lista = ['a', 'b', 'c']
print(lista)

lista2 = lista.copy()
print(lista2)

lista2.append('d')
lista.append('e')
print(lista)
print(lista2)
