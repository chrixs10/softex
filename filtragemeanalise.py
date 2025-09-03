vendas = [
    ("Teclado", 50, 2),
    ("Mouse", 25.50, 4),
    ("Fone", 45, 1 ),
    ("Webcam", 75.20, 2),
    ('Monitor',300, 1 ),
    ]
vendas_filtradas = list()
produtos_unicos = set()

for produto, valor, quantidade in vendas:
    valor_total = valor * quantidade
    if valor_total >= 100:
        vendas_filtradas.append((produto, valor, quantidade))
    produtos_unicos.add(produto)
    
print("Vendas filtradas de valores maior que 100: ")
if vendas_filtradas:
    for produto,  valor, quantidade in vendas_filtradas:
        valor_total = valor * quantidade
        print(f"{produto}: {quantidade} x R${valor:.2f} = R${valor_total:2f}")
else:
    print("nenhuma venda atingiu R$100! ")