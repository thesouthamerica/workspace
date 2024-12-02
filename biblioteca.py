from abc import ABC, abstractmethod

# Classe base Pessoa
class Pessoa(ABC):
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

# Classe UsuarioComum
class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade, matricula)
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if len(self.livros_emprestados) < 3 and livro.disponivel:
            self.livros_emprestados.append(livro)
            livro.emprestar()
            print(f"{self.nome} emprestou o livro '{livro.titulo}'")
        else:
            print("Não foi possível emprestar o livro.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.devolver()
            print(f"{self.nome} devolveu o livro '{livro.titulo}'")
        else:
            print("O livro não está na lista de empréstimos.")

# Classe Administrador
class Administrador(Pessoa):
    def cadastrar_usuario(self, nome, idade, matricula):
        return UsuarioComum(nome, idade, matricula)

    def cadastrar_livro(self, titulo, autor, ano):
        return Livro(titulo, autor, ano)

# Classe base ItemBiblioteca
class ItemBiblioteca(ABC):
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

# Classe Livro
class Livro(ItemBiblioteca):
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
        else:
            print("Livro já emprestado.")

    def devolver(self):
        self.disponivel = True

# Testando o sistema
admin = Administrador("Alice", 35, "ADM001")
user = admin.cadastrar_usuario("Carlos", 25, "U001")
livro1 = admin.cadastrar_livro("Python Básico", "Autor A", 2023)

user.emprestar_livro(livro1)
user.devolver_livro(livro1)
