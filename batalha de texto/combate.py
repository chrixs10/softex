import time

def batalha(heroi, monstro):
    while heroi.estar_vivo() and monstro.estar_vivo():
        print(f"\n Vida do héroi: {heroi.vida} | "
            f"Vida do monstro: {monstro.vida}")
        
        print("\n Escolhe sua ação\n",
            "1) Atacar\n",
            "2) Fugir\n",
            "3) Defender\n",
            "4) Usar poção")
        
        escolha = input("Digite a opção escolhida: ")
        if escolha == "1":
            heroi.atacar(monstro)
        elif escolha == "2":
            print(f"{heroi.nome} Fugiu da batalha! ")
        elif escolha == "3":
            heroi.defender()
            print(f"{heroi.nome} está defendendo, dano do proxímo ataque reduzido!! ")
        elif escolha == "4":
            heroi.usar_pocao()
        else:
            print("Escolha inválida!! o turno foi perdido! ")
        if not monstro.estar_vivo():
            print("Herói venceu !!!")
            break

        time.sleep(1) #tempo de esperar pra executar o comando
        monstro.atacar(heroi)

        if not heroi.estar_vivo():
            print("O Monstro venceu!")
            break
        
        time.sleep(1) 


    
