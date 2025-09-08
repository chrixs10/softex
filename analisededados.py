clientes = [
    {"nome": "Christian", "idade": 22, "bairro": "Pedreiras"},
    {"nome": "Maria", "idade": 19, "bairro": "Parque Nanci"},
    {"nome": "Henrique", "idade": 21, "bairro": "Parque Nanci" },
    {"nome": "Nayran","idade": 20, "bairro": "Cajueiro"},
    {"nome": "Francesco", "idade": 50, "bairro": "Flamengo"}
]

print(" -=-=-=-=- | Clientes | -=-=-=--=\n")
for cliente in clientes:
    nome = cliente["nome"]
    idade = cliente["idade"]
    print(f"Nome: {nome}, Idade: {idade}")

soma_idade = 0
total_clientes = 0 

for cliente in clientes:
    soma_idade += cliente["idade"]

total_clientes = len(clientes)
idade_media = soma_idade / total_clientes
print(f"\nIdade média dos clientes: {idade_media:.2f} anos")

clientes_por_cidade = {}

for cliente in clientes:
    cidade = cliente["bairro"]
    if cidade in clientes_por_cidade:
        clientes_por_cidade[cidade] += 1
    else:
        clientes_por_cidade[cidade] = 1

print("\n -=-=-=- | CLIENTES POR CIDADE | -=-=-=-=-")
print(clientes_por_cidade)



