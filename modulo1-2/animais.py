class animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        print("teste")

class cachorro(animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca
    def fazer_som(self):
        print("Auauau")

class gato(animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome,idade)
        self.raca = raca
    def fazer_som(self):
        print("Miau miau")

cao = cachorro("Selena", 4, "Poodle")
gato = gato("Spike", 11, "Vira-láta" )

def emitir_som(animal:animal):
    animal.fazer_som()

emitir_som(cao)
emitir_som(gato)        