# funções utilizadas para comparar um conjunto a outro
print(30 * '-')
print('função union() - união de conjunto')
conjunto1 = {1, 5, 8, 9}
conjunto2 = {3, 6, 2}
conjunto3 = conjunto1.union(conjunto2)
print(conjunto3)
'''
outra possibilidade sem a necessidade de gerar um novo conjunto, como foi gerado acima o conjunto3
conjunto1.update(conjunto2)
print(conjunto1)
'''

print(30 * '-')
print('função intersection() - elementos que realizam a intersecção entre dois conjuntos ')
conjunto1 = {1, 5, 3, 2}
conjunto2 = {3, 6, 2}
conjunto3 = conjunto1.intersection(conjunto2)
print(conjunto3)
'''
outra possibilidade sem a necessidade de gerar um novo conjunto, como foi gerado acima o conjunto3
conjunto1.intersection_update(conjunto2)
print(conjunto1)
'''

print(30 * '-')
print('função symmetric_difference() - elementos que se diferem entre os dois conjuntos ')
conjunto1 = {1, 5, 3, 2}
conjunto2 = {3, 6, 2}
conjunto3 = conjunto1.symmetric_difference(conjunto2)
print(conjunto3)
'''
outra possibilidade sem a necessidade de gerar um novo conjunto, como foi gerado acima o conjunto3
conjunto1.symmetric_difference_update(conjunto2)
print(conjunto1)
'''