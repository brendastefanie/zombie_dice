import random
from collections import namedtuple

#Rotina para receber os jogadores
print("Bem-vindo ao zombie dice! \n")

nom_jogadores = []
nome = ""

try:
    num_jogadores = int(input("Qual a quantidade de jogadores? "))
    if num_jogadores >= 2 and num_jogadores <= 98:
        print("Quantidade de jogadores atendida. Divirtam-se! \n")
    else:
        print("Quantidade de jogadores inválida!")

    for i in range(num_jogadores):
        nome = input("Digite o nome do " + str(i + 1) + "° jogador: ").split()
        nom_jogadores.append(nome)
except ValueError:
    print("Valor inválido, tente novamente!")
#Criando os dados


def copo():
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

pontos = []
for i in range(num_jogadores):
    pontos.append([0, 0])

#print(pontos)
jogador_atual = 0
dado_sorteado = []
pular_passo = 0
dado_passo = []
dados_faltantes = 0
passos = 0
dados = copo()

while True:


    def mostrar_copo(dados):
        """
        Mostra os dados que estão no copo

        :param dados: é a lista de dados que estão no copo
        :return: retorna os dados que estão no copo
        """
        return print("Os dados armazenados no copo são:", dados)


    def remover_dados(rem_dados):
        """
        Remove os dados que foram sorteados

        :param rem_dados: dados que devem ser removidos
        :return: retorna os dados que sobraram dentro do copo após a remoção dos dados sorteados
        """
        dados.pop(rem_dados)
        return dados


    def lancar_dados(quant_dados=3, limite_range=len(dados) - 1):
        """
        Sorteia os dados

        :param quant_dados: quantidade de dados que devem ser sorteados
        :param limite_range: define o limite  de números que devm ser sorteados ao usar a função random
        :return: retorna os dados que foram soreteados e os que sobraram dentro do copo
        """
        #print(limite_range)
        # Sorteando os dados e suas faces
        print("É o turno do", nom_jogadores[jogador_atual])
        mostrar_copo(dados)
        input("Pressione enter para sortear os dados:")
        print("Dados sorteados:")
        for i in range(quant_dados):
            sorteio = random.randint(0, limite_range)
            sorteados = dados[sorteio]
            #print(sorteados)
            cor_dado(sorteados, i)
            dado_sorteado.append(sorteados)
            remover_dados(sorteio)
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


    def sortear_faces(dado_sorteado):
        """
        Sorteia a face do dado

        :param dado_sorteado: dados que foram sorteados
        :return: retorna os pontos que o jogador fez na rodada e o número de faces que foram passos
        """
        passos = 0
        input("Pressione enter para sortear as faces:")
        print("Faces sorteadas:")
        for sorteados in dado_sorteado:
            face = random.randint(0, 5)
            print(sorteados[face])
            print(sorteados)
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
        return pontos, passos


    def pontuacao(pontos):
        """
        Apresenta a pontuação do jogo

        :param pontos: pontuação que o jogador fez
        """
        print("Seu score: ")
        print("Cérebro:", pontos[jogador_atual][0])
        print("Passos:", passos)
        print("Tiros:", pontos[jogador_atual][1])

    if dados_faltantes == 0 and passos == 0 and pular_passo == 0:
        #print(dado_sorteado, 's')
        dado_sorteado, dados = lancar_dados()
    elif dados_faltantes > 0:
        #print(dado_sorteado, 'b')
        dado_sorteado, dados = lancar_dados(dados_faltantes)

    print(dado_sorteado, 'e')
    pontos, passos = sortear_faces(dado_sorteado)
    #print(dado_sorteado)
    print("\n")
    #print(dado_passo)
    input("Pressione enter para prosseguir ")
    print("\n")
    pontuacao_jogo = pontuacao(pontos)
    print("\n")
    if pontos[jogador_atual][1] >= 3:
        pontos.pop(jogador_atual)
        nom_jogadores.pop(jogador_atual)
        print("Você levou 3 tiros! Game over!")
        if jogador_atual == len(nom_jogadores):
            jogador_atual = 0
        if len(nom_jogadores) == 1:
            print("Jogador", nom_jogadores[jogador_atual], "venceu!")
            input("Pressione enter para encerrar: ")
            break
        else:
            passos = 0
            #print(pontos)
            dado_sorteado.clear()
            dados.clear()
            dados = copo()
            dado_passo.clear()
            dados_faltantes = 0
            pular_passo = 0
            print("\n")
    elif pontos[jogador_atual][0] >= 13:
        print("Parabéns, você comeu 13 cérebros. Você venceu o jogo! \n")
        input("Pressione enter para encerrar: ")
        break
    else:
        continuar_passar = ""
        while continuar_passar != 'P' and continuar_passar != 'p' and continuar_passar != 'C' and continuar_passar != 'c':
            continuar_passar = input("Digite C para continuar e P para passar a vez para o próximo jogador: ")
        if continuar_passar == "C" or continuar_passar == "c":
            print(passos)
            if passos > 0 and passos < 3:
                dado_sorteado.clear()
                dado_sorteado = dado_passo
                dados_faltantes = 3 - passos
                print(dado_sorteado)
            elif passos == 3:
                pular_passo = 1
                dados_faltantes = 0
            else:
                dados_faltantes = 3
                dado_sorteado.clear()
            passos = 0
            dado_passo = []
            print("Iniciando mais um turno da rodada atual...")
        elif continuar_passar == "P" or continuar_passar == "p":
            pontos[jogador_atual][1] = 0
            passos = 0
            print("Seu score: ")
            print("Cérebro:", pontos[jogador_atual][0])
            print("Tiros:", pontos[jogador_atual][1])
            #print(pontos)
            if jogador_atual + 1 < len(nom_jogadores):
                jogador_atual += 1
            else:
                jogador_atual = 0
            dado_sorteado.clear()
            dados.clear()
            dados = copo()
            dado_passo.clear()
            dados_faltantes = 0
            pular_passo = 0
            print("\n")
        else:
            print("Houve um erro interno do sistema, estamos trabalhando para arrumá-lo. \n"
                  "Finalizando o jogo! \n")
            input("Pressione enter para encerrar: ")
            break