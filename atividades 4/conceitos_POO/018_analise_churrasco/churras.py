#consumo padrão 0.40kg
#preço 82.40/kg

#from rich import print
from rich.panel import Panel
from rich.traceback import install

install ()

class Churrasco():
    def __init__(self, titulo, convidados):
        painel = Panel
        
        def teste():
            painel(f"alisando {titulo} com {convidados} convidados", title = {titulo})



c1= Churrasco("teste", 12)

print(Churrasco.t)