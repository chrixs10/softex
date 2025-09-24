class Livro:
    def __init__(self, titulo: str, autor:str):
        self.titulo=titulo
        self.autor=autor

class Biblioteca:
    def __init__(self):
        self.acervo=[]


    def adicionar_livro(self,livro):
        self.livro=Livro
        self.acervo.append(livro)  


    def listar_livros(self)-> list:
        for livro in self.acervo:
            print(f"Autor: {livro.autor}\nLivro: {livro.titulo}\n")


livro_1=Livro("Dom Quixote", "Miguel de Cervantes")
livro_2=Livro("A Culpa é das Estrelas", "John Green")

livros=Biblioteca()
livros.adicionar_livro(livro_1)
livros.adicionar_livro(livro_2)

livros.listar_livros()