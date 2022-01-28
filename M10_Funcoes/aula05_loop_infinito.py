# cuidado com os loops infinitos, eles irão gerar sobrecarda de memória e irão quebrar o seu programa

def olamundo():
    print('ola mundo')


def executar():
    olamundo()


executar()
