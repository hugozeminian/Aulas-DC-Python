'''
- Listas:       Coleção ordenada, mutável e que permite valores duplicados
- Tuplas:       Coleção ordenada, imutável e que permite valores duplicados
- Dicionários:  Coleção não ordenada, mutável e que não permite valores duplicados
> Sets:         Coleção não ordenada, imutável e que não permite valores duplicados
'''

# Os sets também são conhecidos como conjuntos

conjunto = {'item1', 'item2', 'item3', 'item3',
            'item2', 'item1', 3, True, 4.7, "são paulo"}
print(type(conjunto))
print(conjunto)                 # dados não ordenados
print(len(conjunto))            # não aceita valores duplicados


tupla1 = (3, 7, 9, 5)  # transformar esta tupla com o construtor do Set
# outros construtuores -> Lista = list;     Tuplas = tuple;     Dicionários = dict

conjunto1 = set(tupla1)
print(conjunto1)

# também é possível passar o valor de uma tupla diretamente para o construtor do set
conjunto2 = set((3, 7, 9, 5))
print(conjunto2)
print(type(conjunto2))

# set não permite referência de indice e chaves, portanto não é possível muda-lo após ter definido este conjunto, exemplo
'''conjunto3 = {3, 7, 9, 5}
print(conjunto3[0]) # isso erá gerar um erro: "TypeError: 'set' object is not subscriptable"
conjunto[0] = 4     # isso erá gerar um erro
'''
# portanto como acessar os itens do conjunto sem imprimir eles por inteiro
# pode ser acessado pelo loop for
conj = {'item1', 'item2', 'item3', 'item4', 'item5'}
for x in conj:
    print(x)

# pode ser acessado pelo operador de associação in
conj2 = {4, 6, 8, 9, 1}
print(6 in conj2) # retorno true
print(5 in conj2) # retorno false
