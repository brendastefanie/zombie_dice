#Nome: Brenda Stefanie Oliveira Saldanha
#Curso: Gestão de Tecnologia da Informação

"""
Módulo da partida
"""

import Jogadores
import Copo


def iniciar_partida(num_jogadores, nom_jogadores):
    """
    Inicia uma nova partida do jogo

    :param num_jogadores: quantidade de jogadores
    :param nom_jogadores: nome dos jogadores
    :return:
    """

    # Inicialização de variáveis que serão usadas durante o jogo
    #Importando os dados do copo
    dados = Copo.iniciar_copo()
    #Importando os pontos dos jogadores
    pontos = Jogadores.pontos_jogador(num_jogadores)
    jogador_atual = 0
    dado_sorteado = []
    pular_passo = 0
    dados_faltantes = 0
    passos = 0

    while True:


        def variaveis_reinicializacao(dados):
            """
            Variáveis que devem ser reinicializadas quando passar para o próximo jogador

            :param dados: dados que sobraram no copo
            :return: retorna as variáveis reinicializadas
            """
            passos = 0
            dado_sorteado.clear()
            dados.clear()
            dados = Copo.iniciar_copo()
            dado_passo.clear()
            dados_faltantes = 0
            pular_passo = 0
            return passos, dado_sorteado, dados, dado_passo, dados_faltantes, pular_passo

        print("É o turno do", nom_jogadores[jogador_atual])
        #Lançamento dos dados
        limite_range = len(dados) - 1
        if dados_faltantes == 0 and passos == 0 and pular_passo == 0:
            dado_sorteado, dados = Copo.lancar_dados(dados, limite_range)
        elif dados_faltantes > 0:
            dado_sorteado, dados = Copo.lancar_dados(dados, limite_range, dado_sorteado, dados_faltantes)

        print("\n")
        #Sorteio das faces
        pontos, passos, dado_passo = Copo.sortear_faces(dado_sorteado, pontos, jogador_atual)
        print("\n")
        #Pontuação dos jogadores assim que as faces são sorteadas
        Jogadores.pontuacao_jogadores(pontos, jogador_atual, passos)
        print("\n")
        #Verifica se o jogador possui 3 tiros ou 13 cérebros
        resultado = Jogadores.valida_vitoria_derrota(pontos, jogador_atual, nom_jogadores)
        if resultado == 0:
            #Reinicializando as variáveis para o próximo jogador
            passos, dado_sorteado, dados, dado_passo, dados_faltantes, pular_passo = variaveis_reinicializacao(dados)
            print("\n")
        #Se há um vencedor finaliza o jogo
        elif resultado == 1:
            break
        #se o jogador não possui 3 tiros ou 13 cérebros, pergunta se ele quer prosseguir ou passar para o próximo
        else:
            continuar_passar = Jogadores.decisao_parar_continuar()
            if continuar_passar == "C" or continuar_passar == "c":
                if passos > 0 and passos < 3:
                    dado_sorteado.clear()
                    dado_sorteado = dado_passo
                    dados_faltantes = 3 - passos
                elif passos == 3:
                    pular_passo = 1
                    dados_faltantes = 0
                else:
                    dados_faltantes = 3
                    dado_sorteado.clear()
                passos = 0
                print("Iniciando mais um turno da rodada atual...")
            elif continuar_passar == "P" or continuar_passar == "p":
                pontos[jogador_atual][1] = 0
                #Mostra o score do jogador atual antes de passar para o próximo
                Jogadores.pontuacao_jogadores(pontos, jogador_atual, passos, continuar_passar)
                #Verifica qual o próximo jogador
                if jogador_atual + 1 < len(nom_jogadores):
                    jogador_atual += 1
                else:
                    jogador_atual = 0
                #Reinicializando as variáveis para o próximo jogador
                passos, dado_sorteado, dados, dado_passo, dados_faltantes, pular_passo = variaveis_reinicializacao(
                    dados)
                print("\n")
            else:
                print("Houve um erro interno do sistema, estamos trabalhando para arrumá-lo. \n"
                      "Finalizando o jogo! \n")
                input("Pressione enter para encerrar: ")
                break


def menu():
    """
    Menu inicial do jogo

    :return: retorna a opção escolhida pelo o usuário
    """
    print("*** Bem-Vindo ao Zombie Dice ***")
    print("1. Iniciar nova partida")
    print("2. Sair")
    op = int(input("Escolha uma das opções: "))
    if 1 <= op <= 2:
        return op
    else:
        print("Opção inválida.")


def inicio_dice(dice_local: dict):
    """
    Inicializa o jogo

    :param dice_local: Variável inicial sendo usada para armazenar os jogadores
    """
    try:
        while True:
            op = menu()
            if op == 1:
                print("\n")
                num_jogadores = Jogadores.inicio_jogadores(dice_local["jogadores"])

                if len(dice_local["jogadores"]) > 0:
                    iniciar_partida(num_jogadores, dice_local["jogadores"])
                    print("\n")
            else:
                break
    except ValueError:
        print("Valor inválido, tente novamente!")
        print("\n")
        inicio_dice(dice_local)


if __name__ == '__main__':
    dice_local = {}
    dice_local["dice"] = {}
    dice_local["jogadores"] = []
    inicio_dice(dice_local)