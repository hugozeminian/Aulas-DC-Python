# index   0         1        2
lista = ['carro', 'barco', 'avião']
print(lista)

for x in lista:
    print(x)

print(len(lista))

for x in range(3):
    print(x)

print(30 * '-')
# portanto, podemos combinar o len() e range() para imprimir o index de uma lista e seus elementos, conforme abaixo:
for x in range(len(lista)):
    print(x, lista[x])

print(30 * '-')
# separando texto de uma string utilizando a função split
texto = 'carro, avião'

lista2 = list(texto)
print(lista2)

texto = texto.split(', ')
print(texto)

# outro exemplo separando uma string
texto = 'meunome@gmail.com'
lista2 = list(texto)
print(lista2)

texto = texto.split('@')
print(texto)

print(30 * '-')
# como adicionar ou remover elementos de minha lista (adicionar elemento função append())
print(lista)
print(len(lista))
# obs.: a função append permite adicionar apenas um elemento por vez
lista.append('moto')
print(lista)
print(len(lista))

for x in range(len(lista)):
    print(x, lista[x])

print(30 * '-')
# também existe a possibilidade de termos uma lista dentro de outra lista
lista.append(['bike', 'kart'])
print(lista)
for x in range(len(lista)):
    print(x, lista[x])

print(30 * '-')
# adicionar elementos em qualquer parte da minha lista e não apenas no final, utilizando a função insert()
lista = ['carro', 'barco', 'avião']
print(lista)

lista.insert(0, 'bicicleta')  # insert(index, elemento)
print(lista)

lista.append(['bicileta', 'navio'])

print(lista)
print(len(lista))

for x in range(len(lista)):
    print(x, lista[x])

print(30 * '-')
print('### extend() ###')
# adicionar elementos de outra lista individualmente em sua 1º lista - função extend()
lista = ['carro', 'barco', 'avião']
print(lista)

lista.extend(['bicicleta', 'navio'])

print(lista)
print(len(lista))

for x in range(len(lista)):
    print(x, lista[x])
