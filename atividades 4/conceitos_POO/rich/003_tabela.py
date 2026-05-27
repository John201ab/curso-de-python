from rich import print
from rich.table import Table

tabela = Table(title=" LISTA DE PREÇOS", style="blue")

tabela.add_column ("nome", justify="right", style="red")
tabela.add_column ("preço", justify="center", style="green")
tabela.add_row ("lápis", "1,50")
tabela.add_row ("borracha","[green] 0,50 [/]")

print(tabela)