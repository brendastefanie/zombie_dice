import random

#Rotina para receber os jogadores
print("Bem-vindo ao zombie dice!")

try:
    qJogadores = int(input("Qual a quantidade de jogadores? "))
    if qJogadores >= 2 and qJogadores <= 98:
        print("Quantidade de jogadores atendida. Divirtam-se!")
    elif qJogadores > 98:
        print("Quantidade de jogadores excedeu!")
    else:
        print("Você precisa de 2 jogadores ou mais!")
except ValueError:
    print("Número inválido, tente novamente!")

#Criando os dados

#Dados verdes
dado_verde1 = 'CPCTPC'
dado_verde2 = 'CPCTPC'
dado_verde3 = 'CPCTPC'
dado_verde4 = 'CPCTPC'
dado_verde5 = 'CPCTPC'
dado_verde6 = 'CPCTPC'
#Dados amarelos
dado_amarelo1 = 'TPCTPC'
dado_amarelo2 = 'TPCTPC'
dado_amarelo3 = 'TPCTPC'
dado_amarelo4 = 'TPCTPC'
#Dados vermelhos
dado_vermelho1 = 'TPTCPT'
dado_vermelho2 = 'TPTCPT'
dado_vermelho3 = 'TPTCPT'

#Sortear 3 dados
sortear_dados = random.randint(1, 3)

#Sortear faces
if sortear_dados == 1:
    sortear_verde = random.randint(1, 6)
    if sortear_verde == 1:
        print(dado_verde1)
    elif sortear_verde == 2:
        print(dado_verde2)
    elif sortear_verde == 3:
        print(dado_verde3)
    elif sortear_verde == 4:
        print(dado_verde4)
    elif sortear_verde == 5:
        print(dado_verde5)
    else:
        print(dado_verde6)
elif sortear_dados == 2:
    sortear_amarelo = random.randint(1, 4)
    if sortear_amarelo == 1:
        print(dado_amarelo1)
    elif sortear_amarelo == 2:
        print(dado_amarelo2)
    elif sortear_amarelo == 3:
        print(dado_amarelo3)
    else:
        print(dado_amarelo4)
else:
    sortear_vermelho = random.randint(1, 4)
    if sortear_vermelho == 1:
        print(dado_vermelho1)
    elif sortear_vermelho == 2:
        print(dado_vermelho2)
    else:
        print(dado_vermelho3)

