# index do string
# o string funciona como cada caractere dentro de um array, então o seu index seria o seguinte:
#       0123456
nome = 'chicago'

print(nome)

# imprimindo cada elemento do string
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[3])
print(nome[4])
print(nome[5])
print(nome[6])

# range(começo, final, incrementa);
for x in range(10, 0, -1):
    print(x)

# imprimindo duas palavras juntas
nome1 = 'Campinas'
nome2 = 'Paulinia'
print(nome1, end=" ")
print(nome2)


# misturando range e strings
nome3 = 'Louyse'
for x in nome3:
    print(x, end="_")
print()
# Extra, troca de variável com recurso do Python (sem precisar de uma memória como mostrado nas aulas anteriores)
print(30 * '-')
x = 5
y = 0
print(x, y)
x, y = y, x
print(x, y)
