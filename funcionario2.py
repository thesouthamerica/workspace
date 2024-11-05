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
            self.exibir_percentual_aumento(valor)
            self.verificar_promocao(salario_antigo)
        else:
            print("Não foi possível corrigir o valor, verifique se tudo está correto e tente novamente.")

    def proventos(self):
        return self._salario

    def exibir_percentual_aumento(self, valor):
        percentual = (valor / (self._salario - valor)) * 100
        print(f"\nO aumento de {funcionario.nome} foi de {percentual:.2f}%.")
    
    def verificar_promocao(self, salario_antigo):
        aumento_percentual = ((self._salario - salario_antigo) / salario_antigo) * 100
        if aumento_percentual >= 25:
            self.promover()

    def promover(self):
        if self.cargo == "Vendedor":
            self.cargo = "Supervisor"
            print(f"Conforme a politica de premiação da empresa, {self.nome} foi promovido(a) a {self.cargo}(a)!\n")
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
            self.ajustar_salario(novo_salario)
            self.exibir_percentual_aumento(valor)
            self.verificar_promocao(salario_antigo)
        else:
            print("Valor de aumento inválido.")

    def ajustar_salario(self, novo_salario):
        self._salario = novo_salario

    def exibir_percentual_aumento(self, valor):
        percentual = (valor / (self._salario - valor)) * 100
        print(f"O aumento foi de {percentual:.2f}%.")
    
    def verificar_promocao(self, salario_antigo):
        aumento_percentual = ((self._salario - salario_antigo) / salario_antigo) * 100
        if aumento_percentual >= 25:
            self.promover()

    def promover(self):
        if self.cargo == "Gerente":
            self.cargo = "Diretor"
            print(f"Conforme a politica de premiação da empresa, {self.nome} foi promovido(a) a {self.cargo}(a)!")
        else:
            print(f"{self.nome} recebeu uma promoção.")

start_time = time.time()

funcionario = Funcionarios("Maria do Bairro", "Vendedor", 2500)
gerente = Gerente("Leonardo Bezerra", "Gerente", 10000)

print(f"O Salario do {funcionario.cargo}, {funcionario.nome} era: R${funcionario._salario:.2f}")
print(f"O Salário do {gerente.cargo}, {gerente.nome} era: R${gerente._salario:.2f}\n")

funcionario.aumentar_salario(800)  
gerente.aumentar_salario(1000)     

print(f"O Salário atual do {funcionario.cargo}, {funcionario.nome} passa a ser: R${funcionario.proventos():.2f}")
print(f"O Salário atual do {gerente.cargo}, {gerente.nome} passa a ser: R${gerente.proventos():.2f}")

end_time = time.time()

execution_time = end_time - start_time
print(f"\nTempo de execução: {execution_time:.5f} segundos")
