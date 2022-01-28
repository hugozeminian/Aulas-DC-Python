''''
Continue = utilizados em laços de repetição

Pass = utilizado em estrutura condicionais

'''

for x in range(10):
    if x == 3:
        continue # significa que irá ignorar a ação do laço (x == 3) e seguirá para  o próximo laço, ou seja x recebe 4
    print(x)

if x == 5:
    pass  # muito cuidado ao utilizar o pass
print('ola mundo')
