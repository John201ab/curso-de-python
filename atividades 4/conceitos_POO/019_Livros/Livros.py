from rich.traceback import install

install()

class Livro():
    def __init__ (self, titulo, pagina):
        self.titulos = titulo
        self.paginas = pagina 
        self.cont = 0
        
    def avancar_pg(self, avanco):
        self.passar=avanco

        while True:
            for c in range (self.passar):
                self.cont += 1
                if self.cont <= self.paginas:
                    print(f"pagina {self.cont} >>")
                else:
                    print(f"Você chegou ao final do livro {self.titulos}!")
                    break
            if self.cont < self.paginas:
                extra = int(input("Digite mais paginas para continuar: "))
                c1.avancar_pg(extra)
            else:
                break

c1=Livro("teste",20)

c1.avancar_pg(5)
