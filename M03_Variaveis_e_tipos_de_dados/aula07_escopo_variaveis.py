# escopo de variáveis

# escopo -> limite, objetivo e propósito de algo, neste caso das variáveis

'''
>variáveis globais
- declaradas fora de todos os blocos de funções
- acessíveis de qualquer local do seu programa
- pode ser usadas e modificadas por qualquer função
- irá existir em toda execução de seu código

>variáveis locais
- declaradas dentro do bloco das funções
- acessíveis dentro de um escopo (não podem ser acessadas ou modificadas por outras funções)
- só existem enquanto a função está sendo executada
'''

x = 5


def funcao():
    x = 3
    print('valor da variável local: ', x)


funcao()
print('valor da variável global:', x)


y = 'Gabriel'  # nome
z = 1.74  # altura
t = '000.000.000-00'  # cpf
l = 23  # idade

nome = 'Gabriel'
altura = 1.74
cpf = '000.000.000-00'
idade = 23
