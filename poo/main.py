#create class product
class Product: 
    def __init__(self, name, price, qtd):
        self.name = name
        self.price = price
        self.qtd = qtd

    def __str__(self):
        return f"produto:{self.name}  Preço: {self.price:.2f}  Quantidade: {self.qtd}"
    
    #metodo update_price
    def update_price (self, new_price):
        self.price = new_price
        print(f"o preço do produto {self.name} foi atualizado para {self.price:.2f}")
    
    #metodo update_qtd
    def update_qtd (self, new_qtd):
        self.qtd = self.qtd-new_qtd
        print(f"A quantidade de unidades em estoque foi atualiazada para {self.qtd}")





#create instace of product
p1 = Product ("laptop", 1000, 5)
#2 = Product ("mouse", 100, 52)
print(p1)
p1.update_price(1200)
p1.update_qtd(4)
print(p1)


#faça uma classe de pessoas com os seguintes atributos: nome, idade, peso e altura.
#crie um metodo para imprimir os dados de uma pessoa
#crie um metodo para calcular quantos anos a pessoa terá daqui a X anos, sendo X um parametro.