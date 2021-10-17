"""
Módulo de Jogadores
"""

jogo_iniciou = 0


def pontos_jogador(num_jogadores):
    """
    Inicializa os pontos dos jogadores

    :param num_jogadores: número de jogadores
    :return: retorna os pontos do jogadores no início da partida
    """
    pontos = []
    for i in range(num_jogadores):
        pontos.append([0, 0])
    return pontos


def decisao_parar_continuar():
    """
    Pergunta se o jogador deseja finalizar seu turno ou continuar a jogar

    :return: retorna a decisão do jogador
    """
    continuar_passar = ""
    while continuar_passar != 'P' and continuar_passar != 'p' and continuar_passar != 'C' and continuar_passar != 'c':
        continuar_passar = input("Digite C para continuar e P para passar a vez para o próximo jogador: ")
    return continuar_passar


def valida_vitoria_derrota(pontos, jogador_atual, nom_jogadores):
    """
    Valida se o jogador perdeu ou venceu

    :param pontos: pontos do jogador atual
    :param jogador_atual: o número do jogador atual
    :param nom_jogadores: o nome do jogador atual
    :return: retorna 1 - Caso tenha saído um vencedor e 0 - Caso o jogador atual levou 3 tiros(perdeu)
    """
    resultado = int
    if pontos[jogador_atual][1] >= 3:
        pontos.pop(jogador_atual)
        nom_jogadores.pop(jogador_atual)
        print("Levou 3 tiros! A partida acabou para você!")
        # Verifica se o anterior a jogar era o último da lista para assim retornar ao primeiro
        if jogador_atual == len(nom_jogadores):
            jogador_atual = 0
        #Caso haja apenas dois jogadores, o jogador que sobrou é declarado vencedor
        if len(nom_jogadores) == 1:
            print("Jogador", nom_jogadores[jogador_atual], "venceu! Parabéns!")
            input("Pressione enter para encerrar: ")
            resultado = 1
        else:
            resultado = 0
    elif pontos[jogador_atual][0] >= 13:
        print("Parabéns, você comeu 13 cérebros. Você venceu o jogo! \n")
        input("Pressione enter para encerrar: ")
        resultado = 1
    return resultado


def pontuacao_jogadores(pontos, jogador_atual, passos=0, continuar_passar=""):
    """
    Apresenta a pontuação do jogo

    :param pontos: pontuação que o jogador fez
    """
    if continuar_passar == "P" or continuar_passar == "p":
        print("Seu score: ")
        print("Cérebro:", pontos[jogador_atual][0])
        print("Tiros:", pontos[jogador_atual][1])
    else:
        print("Seu score: ")
        print("Cérebro:", pontos[jogador_atual][0])
        print("Passos:", passos)
        print("Tiros:", pontos[jogador_atual][1])


def inserir_jogadores(nom_jogadores):
    """
    Insere os jogadores antes de iniciar a partida

    :param nom_jogadores: nome dos jogadores
    :return: retorna a quantidade de jogadores
    """
    try:
        num_jogadores = int(input("Qual a quantidade de jogadores? "))
        validacao = validar_jogadores(num_jogadores, nom_jogadores)

        if validacao:
            print("Quantidade de jogadores atendida. Divirtam-se! \n")
            for i in range(num_jogadores):
                nome = input("Digite o nome do " + str(i + 1) + "° jogador: ").split()
                nom_jogadores.append(nome)
            return num_jogadores
        else:
            print("Quantidade de jogadores inválida!")
            print("\n")
    except ValueError:
        print("Valor inválido, tente novamente!")
        print("\n")


def validar_jogadores(num_jogadores, nom_jogadores):
    """
    Valida se a quanridade de jogadores de 2 a 98

    :param num_jogadores: Quantidade de jogadores
    :param nom_jogadores: Nome dos jogadores
    :return: retorna True caso a quantidade de jogadores é atendida e false caso não seja
    """

    #Caso já exista jogadores e o usuário quer inserir mais um
    if len(nom_jogadores) > 0:
        return True
    else:
        if num_jogadores >= 2 and num_jogadores <= 98:
            return True
        else:
            return False


def menu():
    """
    Menu que visa inicializar os jogadores

    :return: retorna a opção escolhida pelo usuário
    """
    print("*** Jogadores ***")
    print("1. Inserir jogadores")
    print("2. Sair")
    op = int(input("Escolha uma das opções: "))
    if 1 <= op <= 2:
        return op
    else:
        print("Opção inválida.")


def inicio_jogadores(nom_jogadores: list):
    """
    Inicializa os jogadores

    :param nom_jogadores: nome dos jogadores
    :return: retorna a quantidade de jogadores
    """
    while True:
        op = menu()
        if op == 1:
            num_jogadores = inserir_jogadores(nom_jogadores)
        else:
            break
        return num_jogadores


if __name__ == '__main__':
    jogadores_local = []
    inicio_jogadores(jogadores_local)