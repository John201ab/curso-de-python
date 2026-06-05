from rich.traceback import install

install()

class Livro():
    def __init__ (self, titulo, pagina):
        self.titulos = titulo
        self.paginas = pagina
        self.cont = int(0)

    def avancar_pg(self, avanco):
        self.passar=avanco

        while self.cont < self.paginas:
            for cont in range (self.passar):
                self.cont += cont
                print(f"pagina {cont+1} >>")

        if self.passar > self.paginas:
            print(f"Você chegou ao final do livro {self.titulos}!")



c1=Livro("teste",20)

c1.avancar_pg(30)
