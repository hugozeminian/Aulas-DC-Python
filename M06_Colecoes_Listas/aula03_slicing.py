
# index    0        1       2     3    4   5   6  -> ou seja, possui 5 elementos
lista5 = [True, 'chicago', 2.5, False, 4, 10, 111]
print(lista5)


# toda lista possui um índice.
print(lista5[2])

# print(lista5[-6])

# recurso slicing
print(lista5[::])

# print(lista5[ Começo : Fim-1 : incrementa])
print(lista5[1:]) # imprime a partir do indice 1 até o final
print(lista5[2:]) # imprime a partir do indice 2 até o final
print(lista5[:3]) # imprime do começo da lista até o index - 1 (ou seja index 2)
print(lista5[:4]) # imprime do começo da lista até o index - 1 (ou seja index 3)
print(lista5[1:4]) # imprime do primeiro index até o outro index - 1
print(lista5[1:4:1]) # imprime do primeiro index até o outro index - 1, incrementando 1
print(lista5[1:5:3]) # imprime do primeiro index até o outro index - 1, incrementando 2
