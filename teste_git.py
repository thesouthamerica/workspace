class Banco:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def __str__(self):
        return f"\nTitular: {self.titular} \nSaldo: R$ {self.saldo:.2f}"
    
    def deposito (self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"deposito no valor de R${valor:.2f} realizado")
        else:
            print("não foi possivel realizar o depósito")

    def saque (self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print (f"saque no valor de R${valor:.2f} realizado com sucesso")
        else:
            print ("nao foi possivel realizar o saque")
    
    def mostrar_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

correntista1 = Banco ("Leonardo Bezerra", 1000)
print(correntista1)
correntista1.deposito (400)
correntista1.saque (100)
print(correntista1)