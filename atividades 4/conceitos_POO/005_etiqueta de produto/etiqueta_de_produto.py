from rich import print
from rich.table import Table
from rich.traceback import install 

install()

tabela = Table (title="papelaria")
tabela.add_column("produto")
tabela.add_column("preço")

class Catalogo():
    def __init__(self, produto, preco ):
        self.produto = produto
        self.preco = preco

    def nota(self):
        tabela.add_row(self.produto, f"R${self.preco:.2f}")

c1 = Catalogo("lapis", 1.50)
c2 = Catalogo("borracha", 2.50)

c1.nota()
c2.nota()


print(tabela)