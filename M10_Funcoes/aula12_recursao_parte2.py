'''
numeroInt = 5
def reduzirNumero(numeroInt):    
    while numeroInt > 0:
        print(numeroInt)
        numeroInt -= 1


reduzirNumero(7)
'''
'''
Algorítmo
1 - checar se o nosso número não é igual a 0
2 - se ele não for igual a 0, reduzir 1 unidade, 
portanto N - 1
'''

# observe o caminho de ida e de volta da recursividade

'''
def reduzirNumero(numeroInt):
    print(f'print no inicio da função ----> {numeroInt}')
    if numeroInt > 0:
        # N - 1
        reduzirNumero(numeroInt - 1)
        print(f'print no final da função ----> {numeroInt}')


reduzirNumero(5)
'''

# Fatorial sem recursão
def fatorialS(numero):
    fatorial = 1
    if numero == 0:
        return 1
    else:
        for x in range(1, numero + 1):
            fatorial *= x
        return fatorial


print(fatorialS(5))


# Fatorial - Solução Recursiva
def fatorialR(numero):
    if numero == 0: # critério de parada
        return 1
    else:
        # parâmetro da chamada recursiva
        return numero * fatorialR(numero - 1)


print(fatorialR(5))

'''
Cuidados ao utilizar a função recursiva:
- Critério de parada: Determina quando a função deve parar de chamar a si mesma, caso contrário irá entrar em um loop infinito até encher a memória e gerar erro.
- Parâmetro da chamada recursiva: Sofra a alteração para atingir o critério de parada.

O que está ocorrendo na solução recursiva. Olhe as imagens da aula para entender melhor o conceito de pilha que irá ser feito no cálculo.

5! = 5*4!
   = 5*4*3!
   = 5*4*3*2!
   = 5*4*3*2*1!

4! = 4*3!
   = 4*3*2!
   = 4*3*2*1!

3! = 3*2*1
   = 3*2! 

2! = 2*1
   = 2*1!

1! = 1
0! = 1

'''
