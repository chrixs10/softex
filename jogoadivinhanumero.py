numero_secreto = 16
for tentativa in range(5):
    numero = int(input("Digite um numero para adivinhar: "))
    if numero >= 30:
        print("Alto demaiiiissss, tenta tinovo")
    elif numero <= 9:
        print("Baixo demaisssss, tenta tinovo")
    elif numero <= 15:
        print("tá pertinnn, tenta tinovo!!")
    elif numero >= 17:
        print("Passou por poucoooo, tenta tinovo")
    elif numero == numero_secreto:
        print("=== Acerto mizeraviiiii ===")
        break
