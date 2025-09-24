class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular=titular
        self.saldo=saldo_inicial

    def depositar(self,deposito):
        self.saldo+=deposito
    
    def sacar(self,saque):
        if saque<=self.saldo:
            novo_saldo=self.saldo-saque
            print(f"Saque efetuado com sucesso! novo saldo é R${novo_saldo}" )
        else:
            print("Saldo insuficiente")    


usuario=ContaBancaria("Christian" , 50)
print(f"Ola {usuario.titular} seu saldo inicial é R${usuario.saldo}")
saque=float(input("Digite o valor a sacar: R$"))

usuario.sacar(saque)