class Pessoas:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def __str__(self):
        return f"\nNome: {self.name} \nIdade: {self.age} anos \nPeso: {self.weight} Kg \nAltura: {self.height} m\n"

    # Método para atualizar a idade
    def update_age(self, x):
        new_age = self.age + x
        print(f"Daqui a {x} anos, a idade de {self.name} será: {new_age} Anos\n")

    # Método para obter entradas do usuário
    @classmethod
    def create_from_input(cls):
        name = input("Digite o nome: ")
        age = int(input("Digite a idade: "))
        weight = float(input("Digite o peso: "))
        height = float(input("Digite a altura: "))
        return cls(name, age, weight, height)

# Exemplo de uso
p1 = Pessoas.create_from_input()
print(p1)
p1.update_age(20)



#faça uma classe de pessoas com os seguintes atributos: nome, idade, peso e altura.
#crie um metodo para imprimir os dados de uma pessoa
#crie um metodo para calcular quantos anos a pessoa terá daqui a X anos, sendo X um parametro.