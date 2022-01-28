# index      0         1        2
lista = ['item1', 'item2', 'item3']
tupla = ('item1', 'item2', 'item3')

# chave:valor
dicio = {'nome': 'Gabriel', 'ano': 1993, 'valor_logico': True}
print(dicio)

print(30 * '-')
print('### mudar o valor da chave')
dicio['nome'] = 'Hugo'

print(dicio)

print(30 * '-')
print('### método update')
dicio.update({'nome': 'Louyse'})
print(dicio)

print(30 * '-')
print('### adicionar uma nova chave')
dicio['idade'] = 32
print(dicio)

# outra forma
dicio.update({'estado': 'Rio de Janeiro'})
print(dicio)

print(30 * '-')
# apenas da versão 3.7 acima, pois abaixo ele elimina um dado aleatório
print('### funcao popitem - elimina o último item')
dicio.popitem()
print(dicio)

print(30 * '-')
print('### funcao pop - elimina um dado escolhido na chave')
dicio.pop('nome')
print(dicio)

print(30 * '-')
print('### clear - limpa os dados do dicionário')
dicio.clear()
print(dicio)


print(30 * '-')
dicio = {'nome': 'Gabriel', 'ano': 1993, 'valor_logico': True}
print(dicio)
print('### for')
for x, y in dicio.items():
    print(x, y)

print(30 * '-')
print('### copy')
dados = dicio.copy()
print(dicio)
print(dados)
print('### dict')
dicio2 = dict(dados)
print(dicio2)

dados['idade'] = 27
print(dicio)
print(dados)
print(dicio2)
