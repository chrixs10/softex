class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos")

class Estudantes(Pessoas):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, eu tenho {self.idade} e faço curso de {self.curso}.")

curso = Estudantes("Chris", 22, "Engenharia de Software")

pessoa1 = Pessoas("jeff", 22)
pessoa2 = Estudantes("Mari", 19, "medicina")


lista = [curso, pessoa1, pessoa2]
for pessoas in lista:
    pessoas.apresentar()

    