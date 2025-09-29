class Graodecafe:
    def __init__(self):
        pass

    def moer(self):
        print("Moendo os grãos de café!")

class Agua:
    def __init__(self):
        pass
    def aquecer_agua(self):
        print("A água está sendo aquecida!")

class Cafeaocubo:
    def __init__(self):
        self.graodecafe = Graodecafe()
        self.agua = Agua()
    
    def prepararcafe(self):
        print("O Café está sendo preparado!")
        self.graodecafe.moer()
        self.agua.aquecer_agua()
        print("Café está pronto!")

meu_cafe = Cafeaocubo()
meu_cafe.prepararcafe()