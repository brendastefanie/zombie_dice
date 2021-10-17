"""
Módulo dos dados
"""

import random
from collections import namedtuple


def iniciar_copo():
    """
    Inicializa os dados no copo

    :return: retorna os dados que estão no copo
    """
    dados_cores = namedtuple("dados_cores", ["dado_verde", "dado_amarelo", "dado_vermelho"])
    tupla_dados = dados_cores(dado_verde="CPCTPC", dado_amarelo="TPCTPC", dado_vermelho="TPTCPT")
    dados = [tupla_dados[0], tupla_dados[0], tupla_dados[0], tupla_dados[0], tupla_dados[0], tupla_dados[0],
             tupla_dados[1], tupla_dados[1], tupla_dados[1], tupla_dados[1],
             tupla_dados[2], tupla_dados[2], tupla_dados[2]]
    return dados


def remover_dados(rem_dados, dados):
    """
    Remove os dados que foram sorteados do copo

    :param rem_dados: dados que devem ser removidos
    :param dados: dados que estão no copo
    :return: retorna os dados que sobraram dentro do copo após a remoção dos dados sorteados
    """
    dados.pop(rem_dados)
    return dados


def lancar_dados(dados, limite_range, dado_sorteado=[], quant_dados=3):
    """
    Sorteia os dados

    :param dados: dados que estão no copo
    :param limite_range: define o limite  de números que devem ser sorteados ao usar a função random para sortear os dados
    :param dado_sorteado: lista que armazenará os dados sorteados
    :param quant_dados: quantidade de dados que devem ser sorteados
    :return: retorna os dados que foram soreteados e os que sobraram dentro do copo
    """

    print("Os dados armazenados no copo são:", dados)
    input("Pressione enter para sortear os dados:")
    print("Dados sorteados:")
    for i in range(quant_dados):
        sorteio = random.randint(0, limite_range)
        sorteados = dados[sorteio]
        cor_dado(sorteados, i)
        dado_sorteado.append(sorteados)
        remover_dados(sorteio, dados)
        limite_range -= 1
    return dado_sorteado, dados


def cor_dado(sorteados, num_dado):
    """
    Mostra a cor dos dados que foram sorteados

    :param sorteados: dados que foram sorteados
    :param num_dado: número do dado que foi sorteado
    """
    if sorteados == 'CPCTPC':
        print("Dado", str(num_dado + 1) + ": verde.")
    elif sorteados == 'TPCTPC':
        print("Dado", str(num_dado + 1) + ": amarelo.")
    else:
        print("Dado", str(num_dado + 1) + ": vermelho.")


def sortear_faces(dado_sorteado: list, pontos: list, jogador_atual: int):
    """
    Sorteia a face do dado

    :param dado_sorteado: dados que foram sorteados
    :param pontos: pontos atual do jogador
    :return: retorna os pontos que o jogador fez na rodada e o número de faces que foram passos
    """

    dado_passo = []
    passos = 0
    input("Pressione enter para sortear as faces:")
    print("Faces sorteadas:")
    for sorteados in dado_sorteado:
        face = random.randint(0, 5)
        if sorteados[face] == "C":
            pontos[jogador_atual][0] += 1
            print("Você comeu um cérebro")
        elif sorteados[face] == "P":
            passos += 1
            print("Uma vítima escapou")
            dado_passo.append(sorteados)
        else:
            pontos[jogador_atual][1] += 1
            print("Você levou um tiro")
    return pontos, passos, dado_passo


if __name__ == '__main__':
    iniciar_copo()
