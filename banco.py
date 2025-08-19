conta_c = "22215928751"
senha_c = "2701"
saldo = 1000

for tentativa in range(3):
    conta = input("Digite sua conta: ")
    senha = input("Digite sua senha: ")

    if conta == conta_c and senha == senha_c:
        print("Login realizado!!")

        operaçao = input("Digite 's' para saque ou 'd' para deposito").lower()

        if operaçao == 's':
            saque = int(input("Digite o valor do saque: "))
            if saque <= saldo:
               saldo -= saque
               print(f"saque realizado com sucesso, seu saldo atual é: R${saldo}")
               print(f"Valor sacado R${saque}")

            else:
                print("Saldo insuficiente!!!")

        elif operaçao == 'd':
            deposito = int(input("Digite o valor do deposito: "))
            if deposito > 0:
                saldo += deposito
                print(f"Deposito realizado com sucesso. saldo atual: R${saldo}")
            else:
                print("Valor de deposito invalido! ")
        else:
            print("Operação invalida. Use 's' para saque ou 'd' para deposito:   ")
        break 

    else:
        print(f"Conta ou senha incorretos. Tentativas restantes: {2 - tentativa}")
else:
    print("Número de tentativas excedido. TENTE NOVAMENTE MAIS TARDE!")