import time

class Funcionarios:
    def __init__(self, nome, cargo, salario=0):
        self.nome = nome
        self.cargo = cargo
        self._salario = salario

    def aumentar_salario(self, valor):
        if valor > 0:
            salario_antigo = self._salario
            self._salario += valor
            self.exibir_percentual_aumento(valor, salario_antigo)
            self.verificar_promocao(salario_antigo)
            print(f"O Salário do {self.cargo}, {self.nome} é: R${self._salario:.2f}")
        else:
            print("Não foi possível corrigir o valor, verifique se tudo está correto e tente novamente.")

    def proventos(self):
        return self._salario

    def exibir_percentual_aumento(self, valor, salario_antigo):
        if salario_antigo > 0:
            percentual = (valor / salario_antigo) * 100
            print(f"\nO Aumento de {self.nome} foi de R$ {valor:.2f} ou seja, {percentual:.2f}%.")
        else:
            print("Salário antigo não disponível para cálculo de percentual.")
    
    def verificar_promocao(self, salario_antigo):
        aumento_percentual = ((self._salario - salario_antigo) / salario_antigo) * 100
        if aumento_percentual >= 30:
            self.promover()

    def promover(self):
        if self.cargo == "Vendedor":
            self.cargo = "Supervisor"
            print(f"                    <*** Conforme a politica de premiação da empresa, {self.nome} foi promovido(a) a {self.cargo}(a)! ***>")
        elif self.cargo == "Supervisor":
            self.cargo = "Gerente"
            print(f"Conforme a politica de premiação da empresa, {self.nome} foi promovido a {self.cargo}!(a)")
        else:
            print(f"{self.nome} recebeu uma promoção.")

class Gerente(Funcionarios): 
    def __init__(self, nome, cargo, salario=0):
        super().__init__(nome, cargo, salario)

    def aumentar_salario(self, valor):
        if valor > 0:
            salario_antigo = self._salario
            novo_salario = self.proventos() + valor
            self._salario = novo_salario
            self.exibir_percentual_aumento(valor, salario_antigo)
            self.verificar_promocao(salario_antigo)
            print(f"O Salário atual do {self.cargo}, {self.nome} foi alterado para: R${self.proventos():.2f}")
        else:
            print("Valor de aumento inválido.")

    def exibir_percentual_aumento(self, valor, salario_antigo):
        if salario_antigo > 0:
            percentual = (valor / salario_antigo) * 100
            print(f"\nO aumento do {self.cargo} {self.nome} foi de R$ {valor:.2f}, ou seja: {percentual:.2f}%.")
        else:
            print(f"O {self.cargo} {self.nome} não possui um salário válido para cálculo de aumento.")

    def promover(self):
        if self.cargo == "Gerente":
            self.cargo = "Diretor"
            print(f"Conforme a politica de premiação da empresa, {self.nome} foi promovido(a) a {self.cargo}(a)!")
        else:
            print(f"{self.nome} recebeu uma promoção.")

start_time = time.time()

funcionario = Funcionarios("Bill Gates", "Vendedor", 1000)
funcionario2 = Funcionarios("Steve Jobs", "Vendedor", 1000)
funcionario3 = Funcionarios("Jeff Besos", "Vendedor", 1000)
gerente = Gerente("Leonardo Bezerra", "Gerente", 10000)

funcionario.aumentar_salario(200) 
funcionario2.aumentar_salario(500)
funcionario3.aumentar_salario(290)
gerente.aumentar_salario(1000)     

print(f"\nO {funcionario.cargo} {funcionario.nome}, recebe atualmente R$ {funcionario._salario}.")
print(f"O {funcionario2.cargo} {funcionario2.nome}, recebe atualmente R$ {funcionario2._salario}.")
print(f"O {funcionario3.cargo} {funcionario3.nome}, recebe atualmente R$ {funcionario3._salario}.")
print(f"O {gerente.cargo} {gerente.nome}, recebe atualmente R$ {gerente._salario}.")
end_time = time.time()

execution_time = end_time - start_time
print(f"\nTempo de execução: {execution_time:.5f} segundos")
