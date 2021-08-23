import random
print(">>>>> BEM VINDO AO JOGO ZUMBIE DICE <<<<<", '\n')
PLAYER1 = ""
PLAYER2 = ""
PLAYER3 = ""
PLAYER4 = ""
PLAYER5 = ""
new_round = 0
while True:
    try:
        players_number = int(input("Informe o número de jogadores (de 2 a 5): "))
        if players_number >= 2 and players_number <= 5:
            break
        else:
            print("São permitidos de 2 a 5 jogadores!")
    except ValueError:
        print("Por favor, digite o número de jogadores.")
print('\n', ">>>>> Digite o nome dos", players_number, "jogadores:")
for i in range(1, players_number + 1):
    player = str(input("Informe o nome do " + str(i) + " jogador: "))
    if i == 1:
        PLAYER1 = player
    elif i == 2:
        PLAYER2 = player
    elif i == 3:
        PLAYER3 = player
    elif i == 4:
        PLAYER4 = player
    elif i == 5:
        PLAYER5 = player
all_while = True
while all_while:
    for round in range(1, 1000000000):
        if new_round != 0:
            print('\n', ">>>>>", PLAYER1, "VOCÊ COMEÇA A RODADA " + str(round) + " <<<<<")
            input(">> PRESSIONE A TECLA ENTER PARA JOGAR OS DADOS:")
        else:
            print('\n', ">>>>>", PLAYER1, "VOCÊ COMEÇA JOGANDO A RODADA 1 <<<<<")
            input(">> PRESSIONE A TECLA ENTER PARA JOGAR OS DADOS:")
        # Referente ao jogador 1
        player1_round1 = True
        while player1_round1:
            print('\n', PLAYER1, ", VOCÊ PEGOU OS SEGUINTES DADOS <<<<<")
            dice1 = random.choice("RRRRRRYYYYGGG")
            dice1_color = ""
            if dice1 == "R":
                dice1_color = "VERMELHO"
            elif dice1 == "Y":
                dice1_color = "AMARELO"
            elif dice1 == "G":
                dice1_color = "VERDE"
            dice2 = random.choice("RRRRRRYYYYGGG")
            dice2_color = ""
            if dice2 == "R":
                dice2_color = "VERMELHO"
            elif dice2 == "Y":
                dice2_color = "VERMELHO"
            elif dice2 == "G":
                dice2_color = "VERMELHO"
            dice3 = random.choice("RRRRRRYYYYGGG")
            dice3_color = ""
            if dice3 == "R":
                dice3_color = "VERMELHO"
            elif dice3 == "Y":
                dice3_color = "VERMELHO"
            elif dice3 == "G":
                dice3_color = "VERMELHO"
            print(f' | {"DADO 1":^12} | {"DADO 2":^12} | {"DADO 3":^12} |')
            print(f' | {dice1_color:^12} | {dice2_color:^12} | {dice3_color:^12} |')
            print('\n', ">>>>> ", PLAYER1, ", PRESSIONE A TECLA ENTER PARA JOGAR OS DADOS <<<<<")
            play_dices = str(input())
            # --------------------------------------------------------------------------------
            type1 = ""
            if dice1 == "R":
                dice1_type = random.choice("TTTPCC")
                if dice1_type == "T":
                    type1 = "TIRO"
                elif dice1_type == "P":
                    type1 = "FUGIU"
                elif dice1_type == "C":
                    type1 = "CÉREBRO"
            elif dice1 == "Y":
                dice1_type = random.choice("TTPPCC")
                if dice1_type == "T":
                    type1 = "TIRO"
                elif dice1_type == "P":
                    type1 = "FUGIU"
                elif dice1_type == "C":
                    type1 = "CÉREBRO"
            elif dice1 == "G":
                dice1_type = random.choice("TTPCCC")
                if dice1_type == "T":
                    type1 = "TIRO"
                elif dice1_type == "P":
                    type1 = "FUGIU"
                elif dice1_type == "C":
                    type1 = "CÉREBRO"
            # --------------------------------------------------------------------------------
            type2 = ""
            if dice2 == "R":
                dice2_type = random.choice("TTTPCC")
                if dice2_type == "T":
                    type2 = "TIRO"
                elif dice2_type == "P":
                    type2 = "FUGIU"
                elif dice2_type == "C":
                    type2 = "CÉREBRO"
            elif dice2 == "Y":
                dice2_type = random.choice("TTPPCC")
                if dice2_type == "T":
                    type2 = "TIRO"
                elif dice2_type == "P":
                    type2 = "FUGIU"
                elif dice2_type == "C":
                    type2 = "CÉREBRO"
            elif dice2 == "G":
                dice2_type = random.choice("TTPCCC")
                if dice2_type == "T":
                    type2 = "TIRO"
                elif dice2_type == "P":
                    type2 = "FUGIU"
                elif dice2_type == "C":
                    type2 = "CÉREBRO"
            # --------------------------------------------------------------------------------
            type3 = ""
            if dice3 == "R":
                dice3_type = random.choice("TTTPCC")
                if dice3_type == "T":
                    type3 = "TIRO"
                elif dice3_type == "P":
                    type3 = "FUGIU"
                elif dice3_type == "C":
                    type3 = "CÉREBRO"
            elif dice3 == "Y":
                dice3_type = random.choice("TTPPCC")
                if dice3_type == "T":
                    type3 = "TIRO"
                elif dice3_type == "P":
                    type3 = "FUGIU"
                elif dice3_type == "C":
                    type3 = "CÉREBRO"
            elif dice3 == "G":
                dice3_type = random.choice("TTPCCC")
                if dice3_type == "T":
                    type3 = "TIRO"
                elif dice3_type == "P":
                    type3 = "FUGIU"
                elif dice3_type == "C":
                    type3 = "CÉREBRO"
            # --------------------------------------------------------------------------------
            print(f' | {"TIPO DO DADO 1":^12} | {"TIPO DO DADO 2":^12} | {"TIPO DO DADO 3":^12} |')
            print(f'  {type1:^15}  {type2:^15}  {type3:^15} ')
            # Contabilizacão
            shot = 0
            brain = 0
            step = 0
            # Tiros
            if type1 == "TIRO":
                shot += 1
            if type2 == "TIRO":
                shot += 1
            if type3 == "TIRO":
                shot += 1
            # Cérebros
            if type1 == "CÉREBRO":
                brain += 1
            if type2 == "CÉREBRO":
                brain += 1
            if type3 == "CÉREBRO":
                brain += 1
            # Passos
            if type1 == "FUGIU":
                step += 1
            if type2 == "FUGIU":
                step += 1
            if type3 == "FUGIU":
                step += 1
            print('\n', ">>>>> SUA PONTUAÇÃO NESSA RODADA:")
            print("TIROS: ", shot)
            print("CÉREBROS: ", brain)
            print("FUGA: ", step)
            print('\n', ">>>>> QUANTIDADE TOTAL DE CÉREBROS: ")
            print("CÉREBROS: ", brain)
            print('\n', ">>>>> VOCÊ DESEJA CONTINUAR OU PARAR,", PLAYER1, "?")
            while True:
                try:
                    c_p = str(input(">> DIGITE 'C' PARA CONTINUAR OU 'P' PARA PASSAR A VEZ: "))
                    if c_p == "C" or c_p == "c":
                        break
                    elif c_p == "P" or c_p == "p":
                        break
                    else:
                        print(">> Por favor, digite um caracter válido!")
                except:
                    print(">> Por favor, digite um caracter válido!")
            break
        # Referente ao jogador 2
        print('\n', ">>>>>", PLAYER2, "AGORA É SUA VEZ DE JOGAR <<<<<")
        input(">> PRESSIONE A TECLA ENTER PARA PEGAR OS DADOS:")
        player2_round2 = True
        while player2_round2:
            print('\n', PLAYER2, ", VOCÊ PEGOU OS SEGUINTES DADOS <<<<<")
            dice1 = random.choice("RRRRRRYYYYGGG")
            dice1_color = ""
            if dice1 == "R":
                dice1_color = "VERMELHO"
            elif dice1 == "Y":
                dice1_color = "AMARELO"
            elif dice1 == "G":
                dice1_color = "VERDE"
            dice2 = random.choice("RRRRRRYYYYGGG")
            dice2_color = ""
            if dice2 == "R":
                dice2_color = "VERMELHO"
            elif dice2 == "Y":
                dice2_color = "VERMELHO"
            elif dice2 == "G":
                dice2_color = "VERMELHO"
            dice3 = random.choice("RRRRRRYYYYGGG")
            dice3_color = ""
            if dice3 == "R":
                dice3_color = "VERMELHO"
            elif dice3 == "Y":
                dice3_color = "VERMELHO"
            elif dice3 == "G":
                dice3_color = "VERMELHO"
            print(f' | {"DADO 1":^12} | {"DADO 2":^12} | {"DADO 3":^12} |')
            print(f' | {dice1_color:^12} | {dice2_color:^12} | {dice3_color:^12} |')
            print('\n', ">>>>> ", PLAYER2, ", PRESSIONE A TECLA ENTER PARA JOGAR OS DADOS <<<<<")
            play_dices = str(input())
            # --------------------------------------------------------------------------------
            type1 = ""
            if dice1 == "R":
                dice1_type = random.choice("TTTPCC")
                if dice1_type == "T":
                    type1 = "TIRO"
                elif dice1_type == "P":
                    type1 = "FUGIU"
                elif dice1_type == "C":
                    type1 = "CÉREBRO"
            elif dice1 == "Y":
                dice1_type = random.choice("TTPPCC")
                if dice1_type == "T":
                    type1 = "TIRO"
                elif dice1_type == "P":
                    type1 = "FUGIU"
                elif dice1_type == "C":
                    type1 = "CÉREBRO"
            elif dice1 == "G":
                dice1_type = random.choice("TTPCCC")
                if dice1_type == "T":
                    type1 = "TIRO"
                elif dice1_type == "P":
                    type1 = "FUGIU"
                elif dice1_type == "C":
                    type1 = "CÉREBRO"
            # --------------------------------------------------------------------------------
            type2 = ""
            if dice2 == "R":
                dice2_type = random.choice("TTTPCC")
                if dice2_type == "T":
                    type2 = "TIRO"
                elif dice2_type == "P":
                    type2 = "FUGIU"
                elif dice2_type == "C":
                    type2 = "CÉREBRO"
            elif dice2 == "Y":
                dice2_type = random.choice("TTPPCC")
                if dice2_type == "T":
                    type2 = "TIRO"
                elif dice2_type == "P":
                    type2 = "FUGIU"
                elif dice2_type == "C":
                    type2 = "CÉREBRO"
            elif dice2 == "G":
                dice2_type = random.choice("TTPCCC")
                if dice2_type == "T":
                    type2 = "TIRO"
                elif dice2_type == "P":
                    type2 = "FUGIU"
                elif dice2_type == "C":
                    type2 = "CÉREBRO"
            # --------------------------------------------------------------------------------
            type3 = ""
            if dice3 == "R":
                dice3_type = random.choice("TTTPCC")
                if dice3_type == "T":
                    type3 = "TIRO"
                elif dice3_type == "P":
                    type3 = "FUGIU"
                elif dice3_type == "C":
                    type3 = "CÉREBRO"
            elif dice3 == "Y":
                dice3_type = random.choice("TTPPCC")
                if dice3_type == "T":
                    type3 = "TIRO"
                elif dice3_type == "P":
                    type3 = "FUGIU"
                elif dice3_type == "C":
                    type3 = "CÉREBRO"
            elif dice3 == "G":
                dice3_type = random.choice("TTPCCC")
                if dice3_type == "T":
                    type3 = "TIRO"
                elif dice3_type == "P":
                    type3 = "FUGIU"
                elif dice3_type == "C":
                    type3 = "CÉREBRO"
            # --------------------------------------------------------------------------------
            print(f' | {"TIPO DO DADO 1":^12} | {"TIPO DO DADO 2":^12} | {"TIPO DO DADO 3":^12} |')
            print(f'  {type1:^15}  {type2:^15}  {type3:^15} ')
            # Contabilizacão
            shot = 0
            brain = 0
            step = 0
            # Tiros
            if type1 == "TIRO":
                shot += 1
            if type2 == "TIRO":
                shot += 1
            if type3 == "TIRO":
                shot += 1
            # Cérebros
            if type1 == "CÉREBRO":
                brain += 1
            if type2 == "CÉREBRO":
                brain += 1
            if type3 == "CÉREBRO":
                brain += 1
            # Passos
            if type1 == "FUGIU":
                step += 1
            if type2 == "FUGIU":
                step += 1
            if type3 == "FUGIU":
                step += 1
            print('\n', ">>>>> SUA PONTUAÇÃO NESSA RODADA:")
            print("TIROS: ", shot)
            print("CÉREBROS: ", brain)
            print("FUGA: ", step)
            print('\n', ">>>>> QUANTIDADE TOTAL DE CÉREBROS: ")
            print("CÉREBROS: ", brain)
            print('\n', ">>>>> VOCÊ DESEJA CONTINUAR OU PARAR,", PLAYER2, "?")
            while True:
                try:
                    c_p = str(input(">> DIGITE 'C' PARA CONTINUAR OU 'P' PARA PASSAR A VEZ: "))
                    if c_p == "C" or c_p == "c":
                        break
                    elif c_p == "P" or c_p == "p":
                        break
                    else:
                        print(">> Por favor, digite um caracter válido!")
                except:
                    print(">> Por favor, digite um caracter válido!")
            break
        # Referente ao jogador 3
        if players_number >= 3:
            print('\n', ">>>>>", PLAYER3, "AGORA É SUA VEZ DE JOGAR <<<<<")
            input(">> PRESSIONE A TECLA ENTER PARA PEGAR OS DADOS:")
            player3_round3 = True
            while player3_round3:
                print('\n', PLAYER3, ", VOCÊ PEGOU OS SEGUINTES DADOS <<<<<")
                dice1 = random.choice("RRRRRRYYYYGGG")
                dice1_color = ""
                if dice1 == "R":
                    dice1_color = "VERMELHO"
                elif dice1 == "Y":
                    dice1_color = "AMARELO"
                elif dice1 == "G":
                    dice1_color = "VERDE"
                dice2 = random.choice("RRRRRRYYYYGGG")
                dice2_color = ""
                if dice2 == "R":
                    dice2_color = "VERMELHO"
                elif dice2 == "Y":
                    dice2_color = "VERMELHO"
                elif dice2 == "G":
                    dice2_color = "VERMELHO"
                dice3 = random.choice("RRRRRRYYYYGGG")
                dice3_color = ""
                if dice3 == "R":
                    dice3_color = "VERMELHO"
                elif dice3 == "Y":
                    dice3_color = "VERMELHO"
                elif dice3 == "G":
                    dice3_color = "VERMELHO"
                print(f' | {"DADO 1":^12} | {"DADO 2":^12} | {"DADO 3":^12} |')
                print(f' | {dice1_color:^12} | {dice2_color:^12} | {dice3_color:^12} |')
                print('\n', ">>>>> ", PLAYER3, ", PRESSIONE A TECLA ENTER PARA JOGAR OS DADOS <<<<<")
                play_dices = str(input())
                # --------------------------------------------------------------------------------
                type1 = ""
                if dice1 == "R":
                    dice1_type = random.choice("TTTPCC")
                    if dice1_type == "T":
                        type1 = "TIRO"
                    elif dice1_type == "P":
                        type1 = "FUGIU"
                    elif dice1_type == "C":
                        type1 = "CÉREBRO"
                elif dice1 == "Y":
                    dice1_type = random.choice("TTPPCC")
                    if dice1_type == "T":
                        type1 = "TIRO"
                    elif dice1_type == "P":
                        type1 = "FUGIU"
                    elif dice1_type == "C":
                        type1 = "CÉREBRO"
                elif dice1 == "G":
                    dice1_type = random.choice("TTPCCC")
                    if dice1_type == "T":
                        type1 = "TIRO"
                    elif dice1_type == "P":
                        type1 = "FUGIU"
                    elif dice1_type == "C":
                        type1 = "CÉREBRO"
                # --------------------------------------------------------------------------------
                type2 = ""
                if dice2 == "R":
                    dice2_type = random.choice("TTTPCC")
                    if dice2_type == "T":
                        type2 = "TIRO"
                    elif dice2_type == "P":
                        type2 = "FUGIU"
                    elif dice2_type == "C":
                        type2 = "CÉREBRO"
                elif dice2 == "Y":
                    dice2_type = random.choice("TTPPCC")
                    if dice2_type == "T":
                        type2 = "TIRO"
                    elif dice2_type == "P":
                        type2 = "FUGIU"
                    elif dice2_type == "C":
                        type2 = "CÉREBRO"
                elif dice2 == "G":
                    dice2_type = random.choice("TTPCCC")
                    if dice2_type == "T":
                        type2 = "TIRO"
                    elif dice2_type == "P":
                        type2 = "FUGIU"
                    elif dice2_type == "C":
                        type2 = "CÉREBRO"
                # --------------------------------------------------------------------------------
                type3 = ""
                if dice3 == "R":
                    dice3_type = random.choice("TTTPCC")
                    if dice3_type == "T":
                        type3 = "TIRO"
                    elif dice3_type == "P":
                        type3 = "FUGIU"
                    elif dice3_type == "C":
                        type3 = "CÉREBRO"
                elif dice3 == "Y":
                    dice3_type = random.choice("TTPPCC")
                    if dice3_type == "T":
                        type3 = "TIRO"
                    elif dice3_type == "P":
                        type3 = "FUGIU"
                    elif dice3_type == "C":
                        type3 = "CÉREBRO"
                elif dice3 == "G":
                    dice3_type = random.choice("TTPCCC")
                    if dice3_type == "T":
                        type3 = "TIRO"
                    elif dice3_type == "P":
                        type3 = "FUGIU"
                    elif dice3_type == "C":
                        type3 = "CÉREBRO"
                # --------------------------------------------------------------------------------
                print(f' | {"TIPO DO DADO 1":^12} | {"TIPO DO DADO 2":^12} | {"TIPO DO DADO 3":^12} |')
                print(f'  {type1:^15}  {type2:^15}  {type3:^15} ')
                # Contabilizacão
                shot = 0
                brain = 0
                step = 0
                # Tiros
                if type1 == "TIRO":
                    shot += 1
                if type2 == "TIRO":
                    shot += 1
                if type3 == "TIRO":
                    shot += 1
                # Cérebros
                if type1 == "CÉREBRO":
                    brain += 1
                if type2 == "CÉREBRO":
                    brain += 1
                if type3 == "CÉREBRO":
                    brain += 1
                # Passos
                if type1 == "FUGIU":
                    step += 1
                if type2 == "FUGIU":
                    step += 1
                if type3 == "FUGIU":
                    step += 1
                print('\n', ">>>>> SUA PONTUAÇÃO NESSA RODADA:")
                print("TIROS: ", shot)
                print("CÉREBROS: ", brain)
                print("FUGA: ", step)
                print('\n', ">>>>> QUANTIDADE TOTAL DE CÉREBROS: ")
                print("CÉREBROS: ", brain)
                print('\n', ">>>>> VOCÊ DESEJA CONTINUAR OU PARAR,", PLAYER3, "?")
                while True:
                    try:
                        c_p = str(input(">> DIGITE 'C' PARA CONTINUAR OU 'P' PARA PASSAR A VEZ: "))
                        if c_p == "C" or c_p == "c":
                            break
                        elif c_p == "P" or c_p == "p":
                            player3_round3 = True
                            break
                        else:
                            print(">> Por favor, digite um caracter válido!")
                    except:
                        print(">> Por favor, digite um caracter válido!")
                break
        # Referente ao jogador 4
        if players_number >= 4:
            print('\n', ">>>>>", PLAYER4, "AGORA É SUA VEZ DE JOGAR <<<<<")
            input(">> PRESSIONE A TECLA ENTER PARA PEGAR OS DADOS:")
            player1_round1 = True
            while player1_round1:
                print('\n', PLAYER4, ", VOCÊ PEGOU OS SEGUINTES DADOS <<<<<")
                dice1 = random.choice("RRRRRRYYYYGGG")
                dice1_color = ""
                if dice1 == "R":
                    dice1_color = "VERMELHO"
                elif dice1 == "Y":
                    dice1_color = "AMARELO"
                elif dice1 == "G":
                    dice1_color = "VERDE"
                dice2 = random.choice("RRRRRRYYYYGGG")
                dice2_color = ""
                if dice2 == "R":
                    dice2_color = "VERMELHO"
                elif dice2 == "Y":
                    dice2_color = "VERMELHO"
                elif dice2 == "G":
                    dice2_color = "VERMELHO"
                dice3 = random.choice("RRRRRRYYYYGGG")
                dice3_color = ""
                if dice3 == "R":
                    dice3_color = "VERMELHO"
                elif dice3 == "Y":
                    dice3_color = "VERMELHO"
                elif dice3 == "G":
                    dice3_color = "VERMELHO"
                print(f' | {"DADO 1":^12} | {"DADO 2":^12} | {"DADO 3":^12} |')
                print(f' | {dice1_color:^12} | {dice2_color:^12} | {dice3_color:^12} |')
                print('\n', ">>>>> ", PLAYER4, ", PRESSIONE A TECLA ENTER PARA JOGAR OS DADOS <<<<<")
                play_dices = str(input())
                # --------------------------------------------------------------------------------
                type1 = ""
                if dice1 == "R":
                    dice1_type = random.choice("TTTPCC")
                    if dice1_type == "T":
                        type1 = "TIRO"
                    elif dice1_type == "P":
                        type1 = "FUGIU"
                    elif dice1_type == "C":
                        type1 = "CÉREBRO"
                elif dice1 == "Y":
                    dice1_type = random.choice("TTPPCC")
                    if dice1_type == "T":
                        type1 = "TIRO"
                    elif dice1_type == "P":
                        type1 = "FUGIU"
                    elif dice1_type == "C":
                        type1 = "CÉREBRO"
                elif dice1 == "G":
                    dice1_type = random.choice("TTPCCC")
                    if dice1_type == "T":
                        type1 = "TIRO"
                    elif dice1_type == "P":
                        type1 = "FUGIU"
                    elif dice1_type == "C":
                        type1 = "CÉREBRO"
                # --------------------------------------------------------------------------------
                type2 = ""
                if dice2 == "R":
                    dice2_type = random.choice("TTTPCC")
                    if dice2_type == "T":
                        type2 = "TIRO"
                    elif dice2_type == "P":
                        type2 = "FUGIU"
                    elif dice2_type == "C":
                        type2 = "CÉREBRO"
                elif dice2 == "Y":
                    dice2_type = random.choice("TTPPCC")
                    if dice2_type == "T":
                        type2 = "TIRO"
                    elif dice2_type == "P":
                        type2 = "FUGIU"
                    elif dice2_type == "C":
                        type2 = "CÉREBRO"
                elif dice2 == "G":
                    dice2_type = random.choice("TTPCCC")
                    if dice2_type == "T":
                        type2 = "TIRO"
                    elif dice2_type == "P":
                        type2 = "FUGIU"
                    elif dice2_type == "C":
                        type2 = "CÉREBRO"
                # --------------------------------------------------------------------------------
                type3 = ""
                if dice3 == "R":
                    dice3_type = random.choice("TTTPCC")
                    if dice3_type == "T":
                        type3 = "TIRO"
                    elif dice3_type == "P":
                        type3 = "FUGIU"
                    elif dice3_type == "C":
                        type3 = "CÉREBRO"
                elif dice3 == "Y":
                    dice3_type = random.choice("TTPPCC")
                    if dice3_type == "T":
                        type3 = "TIRO"
                    elif dice3_type == "P":
                        type3 = "FUGIU"
                    elif dice3_type == "C":
                        type3 = "CÉREBRO"
                elif dice3 == "G":
                    dice3_type = random.choice("TTPCCC")
                    if dice3_type == "T":
                        type3 = "TIRO"
                    elif dice3_type == "P":
                        type3 = "FUGIU"
                    elif dice3_type == "C":
                        type3 = "CÉREBRO"
                # --------------------------------------------------------------------------------
                print(f' | {"TIPO DO DADO 1":^12} | {"TIPO DO DADO 2":^12} | {"TIPO DO DADO 3":^12} |')
                print(f'  {type1:^15}  {type2:^15}  {type3:^15} ')
                # Contabilizacão
                shot = 0
                brain = 0
                step = 0
                # Tiros
                if type1 == "TIRO":
                    shot += 1
                if type2 == "TIRO":
                    shot += 1
                if type3 == "TIRO":
                    shot += 1
                # Cérebros
                if type1 == "CÉREBRO":
                    brain += 1
                if type2 == "CÉREBRO":
                    brain += 1
                if type3 == "CÉREBRO":
                    brain += 1
                # Passos
                if type1 == "FUGIU":
                    step += 1
                if type2 == "FUGIU":
                    step += 1
                if type3 == "FUGIU":
                    step += 1
                print('\n', ">>>>> SUA PONTUAÇÃO NESSA RODADA:")
                print("TIROS: ", shot)
                print("CÉREBROS: ", brain)
                print("FUGA: ", step)
                print('\n', ">>>>> QUANTIDADE TOTAL DE CÉREBROS: ")
                print("CÉREBROS: ", brain)
                print('\n', ">>>>> VOCÊ DESEJA CONTINUAR OU PARAR,", PLAYER4, "?")
                while True:
                    try:
                        c_p = str(input(">> DIGITE 'C' PARA CONTINUAR OU 'P' PARA PASSAR A VEZ: "))
                        if c_p == "C" or c_p == "c":
                            break
                        elif c_p == "P" or c_p == "p":
                            player5_round5 = True
                            break
                        else:
                            print(">> Por favor, digite um caracter válido!")
                    except:
                        print(">> Por favor, digite um caracter válido!")
                break
        # Referente ao jogador 5
        player5_round5 = True
        if players_number >= 5:
            while player5_round5:
                print('\n', ">>>>>", PLAYER5, "AGORA É SUA VEZ DE JOGAR <<<<<")
                input(">> PRESSIONE A TECLA ENTER PARA PEGAR OS DADOS:")
                print('\n', PLAYER5, ", VOCÊ PEGOU OS SEGUINTES DADOS <<<<<")
                dice1 = random.choice("RRRRRRYYYYGGG")
                dice1_color = ""
                if dice1 == "R":
                    dice1_color = "VERMELHO"
                elif dice1 == "Y":
                    dice1_color = "AMARELO"
                elif dice1 == "G":
                    dice1_color = "VERDE"
                dice2 = random.choice("RRRRRRYYYYGGG")
                dice2_color = ""
                if dice2 == "R":
                    dice2_color = "VERMELHO"
                elif dice2 == "Y":
                    dice2_color = "VERMELHO"
                elif dice2 == "G":
                    dice2_color = "VERMELHO"
                dice3 = random.choice("RRRRRRYYYYGGG")
                dice3_color = ""
                if dice3 == "R":
                    dice3_color = "VERMELHO"
                elif dice3 == "Y":
                    dice3_color = "VERMELHO"
                elif dice3 == "G":
                    dice3_color = "VERMELHO"
                print(f' | {"DADO 1":^12} | {"DADO 2":^12} | {"DADO 3":^12} |')
                print(f' | {dice1_color:^12} | {dice2_color:^12} | {dice3_color:^12} |')
                print('\n', ">>>>> ", PLAYER5, ", PRESSIONE A TECLA ENTER PARA JOGAR OS DADOS <<<<<")
                play_dices = str(input())
                # --------------------------------------------------------------------------------
                type1 = ""
                if dice1 == "R":
                    dice1_type = random.choice("TTTPCC")
                    if dice1_type == "T":
                        type1 = "TIRO"
                    elif dice1_type == "P":
                        type1 = "FUGIU"
                    elif dice1_type == "C":
                        type1 = "CÉREBRO"
                elif dice1 == "Y":
                    dice1_type = random.choice("TTPPCC")
                    if dice1_type == "T":
                        type1 = "TIRO"
                    elif dice1_type == "P":
                        type1 = "FUGIU"
                    elif dice1_type == "C":
                        type1 = "CÉREBRO"
                elif dice1 == "G":
                    dice1_type = random.choice("TTPCCC")
                    if dice1_type == "T":
                        type1 = "TIRO"
                    elif dice1_type == "P":
                        type1 = "FUGIU"
                    elif dice1_type == "C":
                        type1 = "CÉREBRO"
                # --------------------------------------------------------------------------------
                type2 = ""
                if dice2 == "R":
                    dice2_type = random.choice("TTTPCC")
                    if dice2_type == "T":
                        type2 = "TIRO"
                    elif dice2_type == "P":
                        type2 = "FUGIU"
                    elif dice2_type == "C":
                        type2 = "CÉREBRO"
                elif dice2 == "Y":
                    dice2_type = random.choice("TTPPCC")
                    if dice2_type == "T":
                        type2 = "TIRO"
                    elif dice2_type == "P":
                        type2 = "FUGIU"
                    elif dice2_type == "C":
                        type2 = "CÉREBRO"
                elif dice2 == "G":
                    dice2_type = random.choice("TTPCCC")
                    if dice2_type == "T":
                        type2 = "TIRO"
                    elif dice2_type == "P":
                        type2 = "FUGIU"
                    elif dice2_type == "C":
                        type2 = "CÉREBRO"
                # --------------------------------------------------------------------------------
                type3 = ""
                if dice3 == "R":
                    dice3_type = random.choice("TTTPCC")
                    if dice3_type == "T":
                        type3 = "TIRO"
                    elif dice3_type == "P":
                        type3 = "FUGIU"
                    elif dice3_type == "C":
                        type3 = "CÉREBRO"
                elif dice3 == "Y":
                    dice3_type = random.choice("TTPPCC")
                    if dice3_type == "T":
                        type3 = "TIRO"
                    elif dice3_type == "P":
                        type3 = "FUGIU"
                    elif dice3_type == "C":
                        type3 = "CÉREBRO"
                elif dice3 == "G":
                    dice3_type = random.choice("TTPCCC")
                    if dice3_type == "T":
                        type3 = "TIRO"
                    elif dice3_type == "P":
                        type3 = "FUGIU"
                    elif dice3_type == "C":
                        type3 = "CÉREBRO"
                # --------------------------------------------------------------------------------
                print(f' | {"TIPO DO DADO 1":^12} | {"TIPO DO DADO 2":^12} | {"TIPO DO DADO 3":^12} |')
                print(f'  {type1:^15}  {type2:^15}  {type3:^15} ')
                # Contabilizacão
                shot = 0
                brain = 0
                step = 0
                # Tiros
                if type1 == "TIRO":
                    shot += 1
                if type2 == "TIRO":
                    shot += 1
                if type3 == "TIRO":
                    shot += 1
                # Cérebros
                if type1 == "CÉREBRO":
                    brain += 1
                if type2 == "CÉREBRO":
                    brain += 1
                if type3 == "CÉREBRO":
                    brain += 1
                # Passos
                if type1 == "FUGIU":
                    step += 1
                if type2 == "FUGIU":
                    step += 1
                if type3 == "FUGIU":
                    step += 1
                print('\n', ">>>>> SUA PONTUAÇÃO NESSA RODADA:")
                print("TIROS: ", shot)
                print("CÉREBROS: ", brain)
                print("FUGA: ", step)
                print('\n', ">>>>> QUANTIDADE TOTAL DE CÉREBROS: ")
                print("CÉREBROS: ", brain)
                print('\n', ">>>>> VOCÊ DESEJA CONTINUAR OU PARAR,", PLAYER5, "?")
                while True:
                    try:
                        c_p = str(input(">> DIGITE 'C' PARA CONTINUAR OU 'P' PARA PASSAR A VEZ: "))
                        if c_p == "C" or c_p == "c":
                            break
                        elif c_p == "P" or c_p == "p":
                            player2_round2 = True
                            break
                        else:
                            print(">> Por favor, digite um caracter válido!")
                    except:
                        print(">> Por favor, digite um caracter válido!")
                new_round = 1
                break