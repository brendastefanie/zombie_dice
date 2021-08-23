import random

#Rotina para receber os jogadores
print("Bem-vindo ao zombie dice!")

try:
    jogadores = int(input("Qual a quantidade de jogadores? "))
    if jogadores >= 2 and jogadores <= 98:
        print("Quantidade de jogadores atendida. Divirtam-se!")
    else:
        print("Quantidade de jogadores inválida!")
except ValueError:
    print("Número inválido, tente novamente!")

#Criando os dados
#V - verde, A - amarelo e W - verde
dados = 'VVVVVVAAAAWWW'
dado_verde = 'CPCTPC'
dado_amarelo = 'TPCTPC'
dado_vermelho = 'TPTCPT'
continuar = 0
cerebro = 0
passos = 0
tiros = 0

for j in range(jogadores):
    jogador_atual = j + 1
    while continuar == 0:
        # Sorteando os dados e suas faces
        print("É a vez do ", str(jogador_atual) + "° jogador")
        for i in range(3):
            dado_sorteado = random.choice(dados)
            if dado_sorteado == 'V':
                face = random.choice(dado_verde)
                if face == 'C':
                    print("Dado", str(i + 1) + ": verde,", "Face: ", "cérebro")
                    cerebro += 1
                elif face == 'P':
                    print("Dado", str(i + 1) + ": verde,", "Face: ", "passos")
                    passos += 1
                else:
                    print("Dado", str(i + 1) + ": verde,", "Face: ", "tiros")
                    tiros += 1
            elif dado_sorteado == 'A':
                face = random.choice(dado_amarelo)
                if face == 'C':
                    print("Dado", str(i + 1) + ": amarelo,", "Face: ", "cérebro")
                    cerebro += 1
                elif face == 'P':
                    print("Dado", str(i + 1) + ": amarelo,", "Face: ", "passos")
                    passos += 1
                else:
                    print("Dado", str(i + 1) + ": amarelo,", "Face: ", "tiros")
                    tiros += 1
            else:
                face = random.choice(dado_vermelho)
                if face == 'C':
                    print("Dado", str(i + 1) + ": vermelho,", "Face: ", "cérebro")
                    cerebro += 1
                elif face == 'P':
                    print("Dado", str(i + 1) + ": vermelho,", "Face: ", "passos")
                    passos += 1
                else:
                    print("Dado", str(i + 1) + ": vermelho,", "Face: ", "tiros")
                    tiros += 1
        print(tiros, passos, cerebro)
        continuar_passar = input("Digite C para continuar e P para passar a vez para o próximo jogador: ")
        if continuar_passar == "C" or continuar_passar == "c":
            print("Iniciando mais uma rodada do turno atual...")
        else:
            jogador_atual = jogador_atual + 1
            cerebro = 0
            passos = 0
            tiros = 0

            if jogador_atual > jogadores:
                print("Finalizando o jogo")
                continuar = 1
                break


