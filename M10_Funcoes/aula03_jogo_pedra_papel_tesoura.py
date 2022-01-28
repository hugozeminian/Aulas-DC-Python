# import random - dessa maneira iria ser importado todas as funções e poderia pesar o jogo, então da forma descrita abaixo está sendo importado apenas a função choice
from random import choice

jogador_vitorias = 0
maq_vitorias = 0


def Opcao_Jogador():
    esc_jogador = input('Escolha Pedra, Papel ou Tesousa')
    esc_jogador.lower()
    if esc_jogador == 'pedra':
        return esc_jogador
    elif esc_jogador == 'papel':
        return esc_jogador
    elif esc_jogador == 'tesoura':
        return esc_jogador
    else:
        print('opção inválita, tente novamente')
        Opcao_Jogador()


def Opcao_Maquina():
    esc_maquina = choice(['pedra', 'papel', 'tesoura'])
    return esc_maquina


while True:

    esc_jogador = Opcao_Jogador()
    esc_maquina = Opcao_Maquina()

    esc_jogador = input('Você quer jogar novamente?')
    if esc_jogador in ['SIM', 'sim', 'S', 's']:
        pass
    elif esc_jogador in ['NAO', 'nao', 'N', 'n']:
        break
    else:
        break
