from rich import print
from rich.panel import Panel

caixa = Panel("[yellow] texto muito criativo[/]:+1:", title = "mensagem", style = "red", width=90)

print(caixa)