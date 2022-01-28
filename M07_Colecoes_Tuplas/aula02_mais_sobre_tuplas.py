lista = ['item1', 'item2']
print(lista)
lista[0] = 'item3'

print(lista)

# isto também não é possível na tupla, porém ela aceita sobreescrever a varivável como um todo. (da mesma forma como variáveis)
print('----')
tupla = ('item1', 'item2')
print(tupla)

tupla = ('item3', 'item4', 'verde')
print(tupla)


# Qual a função da tupla?
# Exemplo: cadastro que não teriam mudanças, como estados
print('----')
uf = ('SP', 'DF', 'GO')
print(type(uf))
print(uf)

# Exemplo: cadastro que não teriam mudanças, meses do ano
print('----')
meses_ano = ('Jan', 'Fev', 'Mar')
print(meses_ano)

# assim como a lista, a tupla guarda diversos tipos de dados
print('----')
tupla2 = (3, 5.0, True)
print(tupla2)

# é possível ter uma tupla com apenas um valor, mas deve ser escrito com a virgula no final
print('----')
tupla3 = ('item')
print(tupla3)
print(type(tupla3))
tupla4 = ('item',)
print(tupla4)
print(type(tupla4))


# transformando a tupla em lista e lista em tupla
print('---- tupla em lista')
tupla5 = ('item1', 'item2', 'item3', 'item4')
lista5 = list(tupla5)
print(tupla5)
print(lista5)

lista5.append('item5')
print(lista5)

tupla5 = tuple(lista5)
print(tupla5)
