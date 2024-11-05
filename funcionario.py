import time

class Funcionarios:
    def __init__(self, nome, cargo, salario=0):
        self.nome = nome
        self.cargo = cargo
        self._salario = salario

    def aumentar_salario(self, valor):
        if valor > 0:
            self._salario += valor
        else:
            print("Não foi possivel corrigir o valor, verifique se tudo está correto e tente novamente")

    def proventos(self):
        return self._salario
    
class Gerente(Funcionarios): 
    def __init__(self, nome, cargo, salario=0):
        super().__init__(nome, cargo, salario)
    
    def aumentar_salario(self, valor):
        if valor > 0:
            novo_salario = self.proventos() + valor 
            self.ajustar_salario(novo_salario)
        else:
            print("Valor de aumento inválido.")

    def ajustar_salario(self, novo_salario):
        self._salario = novo_salario

# Marcando o tempo de início
start_time = time.time()

funcionario = Funcionarios("Maria do Bairro", "Vendedora", 2500)
gerente = Gerente("Maria", "Gerente", 10000)
print(f"O Salario do funcionário era: R${funcionario._salario:.2f}")
print(f"O Salário do Gerente era: R${gerente._salario:.2f}\n")

funcionario.aumentar_salario(250)
gerente.aumentar_salario(1000)

print(f"O Salário atual do Funcionário passa a ser: R${funcionario.proventos():.2f}")
print(f"O Salário atual do Gerente passa a ser: R${gerente.proventos():.2f}")

# Marcando o tempo de fim
end_time = time.time()

# Calculando o tempo total de execução
execution_time = end_time - start_time
print(f"\nTempo de execução: {execution_time:.5f} segundos")
