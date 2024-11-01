class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.foi_lido = False
    
    def marcar_como_lido(self,nome):
        self.foi_lido = True
        print(f"o livro {self.titulo} foi lido por {nome}")


class Leitor:
    def __init__(self, nome):
        self.nome = nome
    
    def ler_livro(self, livro):
        print(f"{self.nome} está lendo o livro {livro.titulo}")
        livro.marcar_como_lido(self.nome)

        
livro1 = Livro("O Senhor dos Anéis")
leitor1 = Leitor("Camila")

leitor1.ler_livro(livro1)