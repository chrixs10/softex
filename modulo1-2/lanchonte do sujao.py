preco_lanche = 15.00
cupom_valido = "SUJOLANCHES".lower()
desconto = 0.15

produto = ""
while produto != "x-sujao":
    produto = input("Digite o nome do produto (x-sujao): ")
    if produto != "x-sujao":
        print("Produto não disponível. Tente novamente.")

tem_cupom = input("Você tem um cupom de desconto? (s/n): ")

preco_final = preco_lanche
if tem_cupom == "s":
    codigo = input("Digite o código do cupom: ")
    if codigo == cupom_valido:
        preco_final = preco_lanche * (1 - desconto)
        print("Cupom aplicado com sucesso!")
    else:
        print("Cupom inválido. Sem desconto.")

print(f"Total a pagar: R$ {preco_final:.2f}")
print("Pedido finalizado. Obrigado pela preferência!")
