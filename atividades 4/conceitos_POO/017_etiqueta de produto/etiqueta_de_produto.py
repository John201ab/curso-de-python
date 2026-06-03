from rich.table import Table
from rich.traceback import install
from rich import print

install()

#CRIAÇAO DA TABELA
tabela = Table(title = "NOTA FISCAL")
tabela.add_column("PRODUTO")
tabela.add_column("PREÇO")


class catalogo:
    def __init__( self, produto, valor):
        self.produto = produto
        self.valor = valor

    #atribuição do item à tabela 
    def cadastro(self):
        tabela.add_row(self.produto, f"R$ {self.valor}")

#criando as instancias(produtos)
c1 = catalogo("lápis", 1.50)

#adicionando os produtos a tabela
c1.cadastro()


#imprime a tabela
print(tabela)