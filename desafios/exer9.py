class Funcionario:
    percentual_bonus = 1.10

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def receberobonus(self):
        self.salario *= Funcionario.percentual_bonus

funcionario1 = Funcionario("Chris", 1234)
funcionario2 = Funcionario("Maria", 300)


funcionario1.receberbonus()
funcionario2.receberbonus()

print(f"{funcionario1.nome} - R$ {funcionario1.salario:.2f}")
print(f"{funcionario2.nome} - R$ {funcionario2.salario:.2f}")