registro_acesso = []
usuarios_certo = set()
usuarios_errado = set()

while True:
    print(" -=-=-=- MENU PRINCIPAL -=-=-=-=꒱\n",
          "\n",
          "1- Inserir novo acesso!\n",
          "2- Ver registros de acesso!\n",
          "3- Sair do sistema!\n")
    
    print("-=-=-=-=- DIGITE A OPÇÃO -=-=-=-")
    menu = input("Opção: ")

    if not menu.isdigit() or int(menu) not in [1, 2, 3]:
        print("Opção inválida. Tente novamente.\n")
        continue

    if menu == "3":
        break

    if menu == "2":
        print("-=-=-=-=- REGISTROS -=-=-=-=-")
        if not registro_acesso:
            print("Nenhum registro de acesso encontrado.\n")
        else:
            for usuario, status, duracao in registro_acesso:
                print(f"Usuário: {usuario}, Status: {status}, Duração: {duracao} minutos\n")
        
        print("Usuários com Acesso Permitido:", usuarios_certo)
        print("Usuários com Acesso Negado:", usuarios_errado)

        tempo = 0
        for nome, status, duracao in registro_acesso:
            if status == "sucesso":
                tempo += duracao
        print(f"Tempo total de acesso permitido: {tempo} minutos\n")
        continue

    print("-=-=-=- USUÁRIO -=-=-=-=")
    usuario_nome = input("Digite o nome do usuário: ").lower()
    if not usuario_nome.isalpha():
        print("Nome inválido! Deve conter apenas letras.\n")
        continue

    print("-=-=-=- STATUS -=-=-=-\n",
          "\n",
          "Selecione o status:\n",
          "1- Acesso Permitido\n",
          "2- Acesso Negado\n")

    opcao = input("Opção: ")
    if not opcao.isdigit() or int(opcao) not in [1, 2]:
        print("Opção inválida! Tente novamente.\n")
        continue

    status = "sucesso" if opcao == "1" else "falha"

    if opcao == "2":
        registro = (usuario_nome, status, 0)
        registro_acesso.append(registro)
        usuarios_errado.add(usuario_nome)
        continue

    print(" -=-=-=- DURAÇÃO DA SESSÃO -=-=-=-")
    duracao = input("Digite a duração da sessão em minutos: ")
    if duracao.isdigit():
        duracao = int(duracao)
    else:
        print("Duração inválida! Tente novamente.")
        continue

    registro = (usuario_nome, status, duracao)
    registro_acesso.append(registro)
    usuarios_certo.add(usuario_nome)

    print(" -=-=-=- REGISTROS ATUALIZADOS -=-=- ")
    for usuario, status, duracao in registro_acesso:
        print(f"Usuário: {usuario}, Status: {status}, Duração: {duracao} minutos\n")

    print("Usuários com Acesso Permitido:", usuarios_certo)
    print("Usuários com Acesso Negado:", usuarios_errado)
    "\n"
    tempo = 0
    for nome, status, duracao in registro_acesso:
        if status == "sucesso":
            tempo += duracao

    print(f"-=-=-=-=- TEMPO TOTAL DE ATIVIDADE:-=-=-=-=-\nTempo total de acesso permitido: {tempo} minutos\n")