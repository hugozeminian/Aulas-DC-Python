# import random - dessa maneira iria ser importado todas as funções e poderia pesar o jogo, então da forma descrita abaixo está sendo importado apenas a função choice
from random import choice

jogador_vitorias = 0
maq_vitorias = 0
empate = 0


def Opcao_Jogador():
    esc_jogador = input('Escolha Pedra, Papel ou Tesousa: ')
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

    print(30 * '-')
    esc_jogador = Opcao_Jogador()
    esc_maquina = Opcao_Maquina()
    print(30 * '-')

    # foi utilizado a \ para quebrar a linha de código que não deve ultrapassar 89 caracteres
    if (esc_jogador == 'pedra') and (esc_maquina == 'tesoura') \
        or (esc_jogador == 'papel') and (esc_maquina == 'pedra') \
            or (esc_jogador == 'tesoura') and (esc_maquina == 'papel'):
        # Jogador ganha
        print(f'Jogador escolheu {esc_jogador} e a Máquina escolheu {esc_maquina} '
              'Resultado: Você Ganhou!')
        jogador_vitorias += 1
    elif esc_jogador == esc_maquina:
        # Empate
        print(f'Jogador escolheu {esc_jogador} e a Máquina escolheu {esc_maquina} '
              'Resultado: Empate!')
        empate += 1
    else:
        # Máquina ganha
        print(f'Jogador escolheu {esc_jogador} e a Máquina escolheu {esc_maquina} '
              'Resultado: Você Perdeu!')
        maq_vitorias += 1

    print(30 * '-')
    print(f'Vitórias do Jogador: {jogador_vitorias}')
    print(f'Vitorias da Máquina: {maq_vitorias}')
    print(f'Empates: {empate}')
    print(f'Total de partidas: {jogador_vitorias + maq_vitorias + empate}')
    print(30 * '-')

    esc_jogador = input('Você quer jogar novamente? ')
    if esc_jogador in ['SIM', 'sim', 'S', 's']:
        pass
    elif esc_jogador in ['NAO', 'nao', 'N', 'n']:
        break
    else:
        break
