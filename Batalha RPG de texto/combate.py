import time

def batalha(heroi, monstro):
    while heroi.estar_vivo() and monstro.estar_vivo():
        print(f"\nVida do herói:{heroi.vida} | " 
              f"Vida do monstro: {monstro.vida}")
        
        print("\nEscolha sua ação\n",
              "1) Atacar\n",
              "2) Fugir\n",
              "3) Defender\n",
              "4) Usar poção")
        
        escolha = input("Digite a opção escolhida:")
        if escolha == "1":
            heroi.atacar(monstro)
        elif escolha == "2":
            print(f"{heroi.nome} fugiu da batalha")
        elif escolha == "3":
            heroi.defender()
            print(f"{heroi.nome} está defendendo no próximo ataque!")
        elif escolha == "4":
            heroi.usar_pocoes()
        else:
            print("Escolha inválida!! O turno foi perdido!")
        if not monstro.estar_vivo():
            print("O herói venceu")
            break

        time.sleep(1) #pausar a execução do programa por um determinado tempo
        monstro.atacar(heroi)

        if not heroi.estar_vivo():
            print("O monstro venceu!!")
            break
        time.sleep(1)