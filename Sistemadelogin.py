logins = [
    ("Pedro", "sucesso"),
    ("Ana", "falha"),
    ("Maria", "sucesso"),
    ("Pedro", "falha"),
    ("Ana", "falha")
]

login_certo = set()
login_errado = set()

for usuario, status in logins:
    if status == "sucesso":
        login_certo.add(usuario)
    elif status == "falha":
        login_errado.add(usuario)

somente_falha = login_errado.difference(login_certo)
em_ambos = login_certo.intersection(login_errado)

print("\nUsuarios com pelo menos um login Bem_sucedido")
print(login_certo)
print("\nUsuarios que tiverem somente logins com falha: ")
print(login_errado)
print("\n Usuarios com sucesso e falha: ")
print(em_ambos)

