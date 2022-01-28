'''
01 - Implemente um programa que receba a idade de uma pessoa e imprima mensagem de
acordo com os critérios:
● Menor de 16 anos: MENOR
● Entre 16 e 18 anos: EMANCIPADO
● Maior de 18 anos: MAIOR


02 - Implemente um programa que receba a idade de um nadador e imprima a sua
categoria seguindo as regras:
Categoria       Idade
Infantil A      5 a 7 anos
Infantil B      8 a 10 anos
Juvenil A       11 a 13 anos
Juvenil B       14 a 17 anos
'''

print('01 - Implemente um programa que receba a idade de uma pessoa e imprima mensagem de acordo com os critérios: ● Menor de 16 anos: MENOR/ ● Entre 16 e 18 anos: EMANCIPADO/ ● Maior de 18 anos: MAIOR')

idade = int(input('Qual a sua idade? '))
if idade < 16:
    print('MENOR')
elif idade >= 16 and idade <= 18:
    print('EMANCIPADO')
elif idade >= 18:
    print('MAIOR')


print('02 - Implemente um programa que receba a idade de um nadador e imprima a sua categoria')
idadeNadador = int(input("Qual a idade do nadador? "))
if idadeNadador >= 5 and idadeNadador <= 7:
    print('Infantil A')
elif idadeNadador >= 8 and idadeNadador <= 10:
    print('Infantil B')
elif idadeNadador >= 11 and idadeNadador <= 13:
    print('Juvenil A')
elif idadeNadador >= 14 and idadeNadador <= 17:
    print('Juvenil B')
else:
    print('Nadador não se enquadra em nenhuma categoria')
