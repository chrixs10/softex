class Cachorro:
    def __init__ (self, nomecachorro, peso, cor_pelo):
        self.nome = nomecachorro
        self.peso = peso
        self.cor = cor_pelo
class Criança:
    def __init__ (self, nomecriança, peso, cor):
        self.nome = nomecriança
        self.peso = peso
        self.cor = cor

rex = Cachorro("Rex", "11kg", "Marrom",)
Selena = Cachorro("Selena", "5kg", "Preta")
Arthur = Criança("Arthur", "16kg", "Branco")

print(f"O Cão {rex.nome}, com o peso: {rex.peso} da cor: {rex.cor}")
print(f"O Cão {Selena.nome}, com o peso {Selena.peso} da cor: {Selena.cor}")
print(f"A criança {Arthur.nome}, com o peso {Arthur.peso}, {Arthur.cor}")


        