class ControleRemoto:
   def __init__(self, cor,altura,largura):
      self.cor = cor
      self.altura = altura
      self.largura = largura

   def __str__(self):
      return f"\nCor: {self.cor} \nAltura: {self.altura} \nLargura: {self.largura}"
       
   def passar_canal (self, botao):
      if botao == "+":
         print ("passar para o proximo canal")
      elif botao == "-":
         print ("Recuar para o canal anterior")

   def volume (self, botao_vol):
      if botao_vol == "+":
         print ("Almenta o volume 5")
      elif botao_vol == "-":
         print ("diminui o volume 5")

controle = ControleRemoto("preto", "15cm", "3cm")
print(controle.cor)
controle.passar_canal ("+")
controle.volume ("-") 


controle2 = ControleRemoto("cinza", "10cm", "3cm")
print(controle2.altura, controle2.cor)