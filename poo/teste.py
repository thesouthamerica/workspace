class bancobancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def __str__ (self):
        return f"\nTitular: {self.titular} \nSaldo: {self.saldo}"

    def depositar (self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"deposito no valor de RS {valor:.2f} efetuado com sucesso.")
        else: 
            print(f"não foi possivel efetuar o depósito")

    def sacar (self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"saque no valor de RS {valor:.2f} foi realizado com sucesso!")
        else:
            print(f"O valor de RS {valor:.2f} não pode ser efetuado por conta do saldo ser inferior ao valor solicitado!")

p1=bancobancaria ("leonardo Bezerra", 1000)
print (p1)
p1.depositar(10)
print(p1)
p1.sacar(200)
print(p1)



    
