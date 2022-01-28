nome = 'Curso de Python'
valor = range(10)

print(nome)
print(valor)

# transformando os elementos de dentro da função range em uma lista
lista7 = list(range(10))
print(lista7)
lista8 = list(valor)
print(lista8)

lista9 = list('Curso de Python')
print(lista9)
lista10 = list(nome)
print(lista10)

elemento = 'P'
if elemento in lista10:
    print('Este elemento esta dentro da lista')
