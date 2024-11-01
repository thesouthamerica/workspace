#create class product
class Pessoas: 
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def __str__(self):
        return f"\nNome:{self.name} \nIdade: {self.age} \nPeso: {self.weight} \nAltura: {self.height}\n"

    #metodo update_age
    def update_age (self, x):
        new_age = self.age + x  
        print(f"Daqui a {x} anos, a idade de {self.name} será: {new_age} Anos\n")
       
p1 = Pessoas ("leonardo", 40, 105, 1.85)
print (p1)
p1.update_age (20)



#faça uma classe de pessoas com os seguintes atributos: nome, idade, peso e altura.
#crie um metodo para imprimir os dados de uma pessoa
#crie um metodo para calcular quantos anos a pessoa terá daqui a X anos, sendo X um parametro.