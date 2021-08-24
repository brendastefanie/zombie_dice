import random

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
dado_verde = 'CPCTPC'
dado_amarelo = 'TPCTPC'
dado_vermelho = 'TPTCPT'
dados = [dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_verde,
         dado_amarelo, dado_amarelo, dado_amarelo, dado_amarelo,
         dado_vermelho, dado_vermelho, dado_vermelho]

cerebro = 0
passos = 0
tiros = 0
jogador_atual = 0
dado_sorteado = []

while True:
    # Sorteando os dados e suas faces
    print("\n")
    print("É a vez do ", nom_jogadores[jogador_atual], "\n")
    print("Dados sorteados:")
    for i in range(0, 3):
        sorteio = random.randint(0, 12)
        sorteados = dados[sorteio]
        if sorteados == 'CPCTPC':
            print("Dado", str(i + 1) + ": verde.")
        elif sorteados == 'TPCTPC':
            print("Dado", str(i + 1) + ": amarelo.")
        else:
            print("Dado", str(i + 1) + ": vermelho.")
        dado_sorteado.append(sorteados)

    print("\n")
    print("Faces sorteadas:")
    for sorteados in dado_sorteado:
        faces = random.randint(0, 5)
        face = sorteados[faces]
        if face == "C":
            cerebro += 1
            print("Você comeu um cérebro")
        elif face == "P":
            passos += 1
            print("Uma vítima escapou")
        else:
            tiros += 1
            print("Você levou um tiro")
    print("\n")
    continuar_passar = input("Digite C para continuar e P para passar a vez para o próximo jogador: ")
    if continuar_passar == "C" or continuar_passar == "c":
        dado_sorteado = []
        print("Iniciando mais uma rodada do turno atual...")
    elif continuar_passar == "P" or continuar_passar == "p":
        jogador_atual += 1
        cerebro = 0
        passos = 0
        tiros = 0
        dado_sorteado = []

        if jogador_atual == len(nom_jogadores):
            print("Finalizando o jogo!")
            break
    else:
        print("Houve um erro interno do sistema, estamos trabalhando para arrumá-lo. \n" 
              "Finalizando o jogo!")
        break