# remover o ultimo elemento da lista
print(30 * '-')
print('### função pop() ###')
print()

# index   0         1        2
lista = ['carro', 'barco', 'avião']
print(lista)

lista.pop()

print(lista)

for x in range(len(lista)):
    print(x, lista[x])


# remover o elemento da lista de um indice específico, ainda com pop
print(30 * '-')
print('### função pop() ###')
print()

# index   0         1        2
lista = ['carro', 'barco', 'avião']
print(lista)

lista.pop(0)

print(lista)

for x in range(len(lista)):
    print(x, lista[x])

# remover algum elemento específico da lista
print(30 * '-')
print('### função remove() ###')
print()

lista = ['carro', 'barco', 'avião']
print(lista)

lista.remove('barco')

print(lista)

for x in range(len(lista)):
    print(x, lista[x])

# remover algum elemento específico da lista
print(30 * '-')
print('### função remove() ###')
print()

lista = ['carro', 'barco', 'avião']
print(lista)

lista.remove('barco')

print(lista)

for x in range(len(lista)):
    print(x, lista[x])


# deletar a lista ou algum elemento - comando del
print(30 * '-')
print('### comando del ###')
print()

# index   0         1        2
lista = ['carro', 'barco', 'avião']
print(lista)

# del lista
# desta maneira acima a lista como um todo é deletada, e poderá gerar um erro no seu código

# del lista[0] # Obs.: desta maneira será deletado apenas o valor do index 0, não irá gerar erro

print(lista)

for x in range(len(lista)):
    print(x, lista[x])

# como deletar a lista e não gerar erro
# possuo um carrinho de compras, quero deletar um produto (elementos), mas não quero apagar o carrinho (lista) - função clear
print(30 * '-')
print('### função clear() ###')
print()

carrinho_de_compras = ['produto1', 'produto2', 'produto3']
print(carrinho_de_compras, 'fim')
carrinho_de_compras.clear()
print(carrinho_de_compras, 'fim')

# organizar em ordem alfabética ou menor para maior - função sort
print(30 * '-')
print('### função sort() ###')
print()

carrinho_de_compras = ['pão', 'carne', 'verdura', 'alface']
print(carrinho_de_compras, 'fim')
carrinho_de_compras.sort()
print(carrinho_de_compras, 'fim')

lista1 = [10, 20, 2, 1, 40]
print(lista1)
lista1.sort()
print(lista1)

# organizar em ordem decrescente - função sort(reverse = true) e função reverse()
print('### função sort(reverse = true) ###')
lista1.sort(reverse=True)
print(lista1)

print('### função reverse() ###')
lista2 = [10, 20, 2, 1, 40]
print(lista2)
lista2.reverse()
print(lista2)

# Ordenação alfabética de nomes maiúsculos e minúsculos - sort(key = str.lower)
print(30 * '-')
print('### função sort() com chave ###')
print()
lista3 = ['Ana', 'Pedro,', 'Marta', 'Clarice', 'beatriz', 'ana clara', 'hugo']
print(lista3)

lista3.sort(key=str.lower)
print(lista3)
