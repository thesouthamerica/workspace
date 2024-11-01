from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f"{self.ano} {self.marca} {self.modelo}"
    
    @abstractmethod
    def combustivel(self):
        pass

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas
    
    def combustivel(self):
        return "Alimentação Elétrica"

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
    
    def combustivel(self):
        return "Gasolina"

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, carga_maxima):
        super().__init__(marca, modelo, ano)
        self.carga_maxima = carga_maxima
    
    def combustivel(self):
        return "Diesel"

class Carroca(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
    
    def combustivel(self):
        return "Milho e Chicote"

def show_info(veiculo):
    print(f"\nDescrição: {veiculo.descricao()}")
    print(f"Tipo de combustível: {veiculo.combustivel()}\n")


carro = Carro("Tesla", "Model Y", 2024, 4)
moto = Moto("Honda", "BIZ", 2018, 99)
caminhao = Caminhao("RAM", "5500", 2020, 6700)
carroça = Carroca("Carroça","do Cicero", 2018, 1)

show_info(carro)
show_info(moto)
show_info(caminhao)
show_info(carroça)
