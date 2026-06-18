from rich import print
from rich.panel import Panel
from rich.traceback import install

install()

games = []

class Ficha():
    def __init__ (self, nome, nick):
        self.nome = nome
        self.nick = nick

    def Add_game(self, jogos):
        games.append(jogos)

    def table(self):
        placa = Panel(f"""nick: {self.nick}
nome: {self.nome}
jogos salvos: {games}""", title = (f"ficha de <{self.nick}>"), expand = False)
        print(placa)

c1 = Ficha("joão", "Johnzera")

c1.Add_game("Gow")
c1.Add_game("COD")

c1.table()