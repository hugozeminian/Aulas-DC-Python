'''
Listas: coleção ordenada, mutável e que permite valores duplicados
Tuplas: coleção ordenada, imutável e que permite valores duplicados
Dicionários: Coleção não ordenada, mutável e que não permite valores duplicados (chaves iguais)
'''
# index      0         1        2
lista = ['item1', 'item2', 'item3']
tupla = ('item1', 'item2', 'item3')

# chave:valor
dicio = {'chave1': 'Gabriel', 'chave2': 1993, 'chave3': True}
print(dicio)

dicionario = {
    'nome': 'Bruna',
    'idade': 27,
    'nacionalidade': 'brasileira',
    'idade': 35
}

print(dicionario)
print(dicionario['nome'])
print(dicionario.get('nome'))

print(30 * '-')
print('metodo keys')
print(dicionario.keys())

print(30 * '-')
print('metodo len')
print(len(dicionario))

print(30 * '-')
print('metodo values')
print(dicionario.values())

if 'idade' in dicionario:
    print('A chave idade existe')

print(30 * '-')
print('metodo itens')
print(dicionario.items())  # irá retornar várias tuplas
