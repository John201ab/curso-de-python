from rich import print
from rich.panel import Panel

caixa = Panel("[white] texto muito criativo[/]", title = "mensagem", style = "red", width=90)

print(caixa)