estoque_principal = [
    ("Camisa", 100),
    ("Calça", 101),
    ("boné", 50),
    ("Tênis", 120),
]
estoque_online = [
    ("Boné", 50)
    ("Calça", 101)
    ("Regata ", 100)
    ("Tênis", 120)
] 

set_principal = set(estoque_principal)
set_online = set(estoque_online)

em_ambos = set_principal.intersection(set_online)
print("Produtos dísponiveis na loja e no site: ")
print("em_ambos")

apenas_loja = set_principal.difference(set_online)
print("\nProdutos disponiveis apenas na loja fisica: ")
print("apenas_loja")

apenas_online = set_online.difference(set_principal)
print("\nProdutos disponiveis apenas no site: ")
print(apenas_online)