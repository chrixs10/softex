
# rodar em loop infinido x
# ter conta e senha (validar) x
# encerrar atendimento 
# cheque especial (limite saldo negativo)
# tentar 3 vezes a senha x
# opções (saque,deposito e saldo)
# alterar senha
# dizer nome de usuario x
# pagar boleto
# ------------------------------------------------------------------------------------------------

conta_user = "222.159.287-51"
senha_user ="30112024"
limite_saldo_n = -500.00
user = "Christian"
saldo = 0 

while True:
    for i in range(3):
        conta =  input("Entre com a sua conta corrente: ")
        senha = input("Digite sua senha: ")
        if conta == conta_user and senha == senha_user:
            print(f"Bem vindo {user}!")
            acesso_permitido = True
            break
        else:
            print("Conta ou senha inválida!! ") 
            acesso_permitido = False
    if not acesso_permitido:
        break

while True:
    opcao = input("Escolha uma opção:\n"\
    "1- Ver Saldo.\n" \
    "2- Sacar valor.\n" \
    "3- Depositar.\n " \
    "4- Pagar Boleto.\n " \
    "5- Alterar senha.\n" \
    "6- Sair.\n")

    if  opcao == "1":
            print(f"Seu saldo atual é de {saldo}")
    elif opcao == "2":
            valor_a_sacar = float(input("Entre com o valor a ser sacado: "))
            if valor_a_sacar <= (saldo + limite_saldo_n):
                  saldo -= valor_a_sacar
                  print("Saldo liberado, retire seu valor!!")
            else:
                  print("Saldo Insuficiente!")
    elif opcao == "3":
            depositar = float(input("Insira o valor a ser depositado: "))
            if depositar > 0:
                  saldo += depositar
            else:
                  print("Valor inválido!")
    elif opcao == "4":
            boleto = float(input("Entre com valor do boleto: "))
            if boleto < (saldo +limite_saldo_n):
                  saldo -= boleto
            else:
                  print("Saldo Insuficiente!!")
    elif opcao == "5":
            senha_antiga = input("Digite a senha antiga: ")
            senha_nova1 = input("Digite a senha nova: ")
            senha_nova2 = input("Digite a senha novamente: ")
            if senha_antiga == senha_user and senha_nova1 == senha_nova2:
                  senha_user = senha_nova1
                  print("Senha atualizada com sucesso")
            else:
                  print("Senha inválida!!")
    elif opcao == "6":
            print("Atendimento finalizado!!! ")
            break
    else:
        print("Opção invalida")
