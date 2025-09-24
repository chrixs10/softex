class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Carro:
    def __init__(self, modelo, motor_potencia):
        self.modelo = modelo
        self.motor = Motor(motor_potencia)

    def exibir_potencia(self):
        print(f"O carro {self.modelo} tem {self.motor.potencia} cavalos de potência.")

carro = Carro("Beetle", 116)
carro.exibir_potencia()