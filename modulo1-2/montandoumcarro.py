class motor:
    def ligar_motor(self):
        print("O motor ligou!")

    def desligar_motor(self):
        print("desligando motor")

class carro:
    def __init__(self):
        self.motor = motor()

    def ligar(self):
        print("O carro está ligando!!")
        self.motor.ligar_motor()

meu_carro = carro()
meu_carro.ligar()