class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def __str__(self):
        return f"\nTitular: {self.titular} \nSaldo: R$ {self.saldo:.2f}"
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido!")
           
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print(f"Saldo insuficiente! O valor de R$ {valor:.2f} solicitado para saque excede o saldo em conta.")

    def mostrar_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

p1 = ContaBancaria("Leonardo Peixoto Xavier Bezerra", 10000)
print(p1)
p1.depositar(1000)
print(p1)
p1.sacar(20000)
print(p1)
