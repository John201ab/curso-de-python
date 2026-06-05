#consumo padrão 0.40kg
#preço 82.40/kg

from rich import print
from rich.panel import Panel
from rich.traceback import install

install ()

#declaração das variaveis
class Churrasco():
    def __init__(self, titulo, convidados):
        self.titulos=titulo
        self.convidado=convidados
        self.valores=32.96
        self.Kilos=0.40*self.convidado
        self.valoresTot=82.40*self.Kilos

#uso das variaveis em função
    def teste(self):
        testes = Panel(f"""alisando {self.titulos} com {self.convidado} convidados
Cada participante comerá 0.4Kg e cada Kg custa R$82.40
Recomendo comprar {self.Kilos:.3f}Kg de carne.
O custo total será: R${self.valoresTot}
Cada pessaoa pagará: {self.valores}""" , title = (self.titulos), expand = False)
        print(testes)

#passagem de parametros
c1 = Churrasco("churras", 100)

#uso da função
c1.teste()