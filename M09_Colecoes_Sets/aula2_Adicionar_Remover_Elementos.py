'''
para avaliar as funções disponíveis, é possível verificar a biblioteca ou simplesmente utilizar o terminal e verificar da seguinte maneira
- abra o terminal e chame o interpretador python (apenas digite python)
- crie um conjunto, exemplo: conj = {2, 4, 7, 8} 
- digite dir(conj)
- irá aparecer todas as funções disponíveis
'''
# adicionar dados ao conjunto:
# cuidado a palavra Set é reservada pelo sistema para o construtor
print('adicionar elementos ao conjunto - função .add()')
set1 = {'item1', 'item2', 'item3'}
print(set1)
set1.add('item5')
print(set1)
set1.add(8)
set1.add(True)
print(set1)

print(30 * '-')
print('adicionar elementos ao conjunto - função .update() - set dentro de outro set')
set2 = {4, 5, 7, 8, 9, 1}
set3 = {'item3', 'item5', 'item1'}
set2.update(set3)
print(set2)

# a função update() também consegue passar para dentro do set qualquer tipo de coleção (tupla, lista, etc) transformando essa coleção em um set também
set4 = {4, 5, 7, 8, 9, 1}
set4.update([1, 4, 7, 8, 9, 3, 'item5', 'item6'])
print(set4)

print(30 * '-')
# não é possível garantir qual item será removido
print('remover elementos dados ao conjunto - função .pop()')
set5 = {4, 5, 7, 8, 9, 1}
set5.update((1, 4, 7, 8, 9, 3, 'item5', 'item6'))
print(set5)

set5.pop()
print(set5)

print(30 * '-')
# é possível escolher o item a ser removido
print('remover elementos dados ao conjunto - função .remove()')
set6 = {4, 5, 7, 8, 9, 1}
set6.update((1, 4, 7, 8, 9, 3, 'item5', 'item6'))
print(set6)

set6.remove('item5')
# set6.remove('item7') # irá gerar um erro
print(set6)

print(30 * '-')
# é possível escolher o item a ser descartado
print('remover elementos dados ao conjunto - função .discard()')
set7 = {4, 5, 7, 8, 9, 1}
set7.update((1, 4, 7, 8, 9, 3, 'item5', 'item6'))
print(set7)

set7.discard('item6')
set7.discard('item7')  # nada acontece
print(set7)

# diferença entre REMOVE e DISCARD, caso tente remover um item que não existe com a função Remove(), ela irá gerar um erro, já a função Discard(), não irá acontecer nada.

print(30 * '-')
print('limpar o set - função .clear()')
# também é possível deletar o set por completo com o del, porém caso ele seja chamado após ser deletado irá gerar erro.
set8 = {4, 5, 7, 8, 9, 1}
set8.update((1, 4, 7, 8, 9, 3, 'item5', 'item6'))
print(set8)

set8.clear()
print(set8)  # irá exibir um set vazio
