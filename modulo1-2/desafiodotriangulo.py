lados = []
for i in range(1, 4):
    while True:
        lado = input(f"Digite o valor do {i}º lado do triângulo: ")
        if lado.isdigit():
            lado = int(lado)
            if lado > 0:
                lados.append(lado)
                break
            else:
                print("Lado inválido! Deve ser um número positivo.")
        else:
            print("Lado inválido! Deve ser um número.")
            
l1, l2, l3 = lados
if (l1 < l2 + l3 and l1 > abs(l2 - l3) and
    l2 < l1 + l3 and l2 > abs(l1 - l3) and
    l3 < l1 + l2 and l3 > abs(l1 - l2)):
    print("Os lados podem formar um triângulo!")
else:
    print("Os lados NÃO podem formar um triângulo.")