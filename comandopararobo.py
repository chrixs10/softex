posicao_robo = 0
while True:
        opcao = input("Escolha uma opção:\n"\
        "1- Avançar.\n"\
        "2- Recuar.\n"\
        "3- Status.\n"\
        "4- Desligar.\n")

        if opcao == "1":
            valor = int(input(" Digite a quantidade de casas que deseja AVANÇAR: "))
            posicao_robo += valor 
            print(f" -=-=-=-=-=-=- O robo andou {valor} de casas. Posição atual: {posicao_robo} -=-=-=-=-=-=-=- ")
        elif opcao == "2":
              valor = int(input(" Digite a quantidade de casas que deseja VOLTAR: "))
              posicao_robo -= valor
              print(f" -=-=-=-=- O Robô voltou {valor} de casas! Posição atual: {posicao_robo} -=-=-=-=-  ")
        elif opcao == "3":
              print(f"-=-=-=-=- O Robo está na posição {posicao_robo} -=-=-=-=-=- ! ")
        elif opcao == "4":
              print("!!!!Encerrando o Sistema!!!")
              break
        else:
              print("Comando invalido! ")