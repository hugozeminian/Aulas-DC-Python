# Argumentos nomeados

def imprimir_nome(nome, sobrenome, idade): # parâmetros obrigatórios
    print(f'nome: {nome}')
    print(f'sobrenome: {sobrenome}')
    print(f'idade: {idade}')


nome = input('Digite o seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
idade = input('Digite a sua idade: ')


imprimir_nome(nome, sobrenome, idade)

# ao utilizar parâmetros nomeados, eles podem estar até fora de ordem que não altera o resultado. exemplo abaixo
imprimir_nome(idade=29, nome='Louyse', sobrenome='Anjos')
imprimir_nome(idade=idade, nome=nome, sobrenome=sobrenome)
