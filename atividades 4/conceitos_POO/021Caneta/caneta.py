from rich import print
from rich.traceback import install

install()

class Caneta():

    tampa = True

    def __init__(self, cor):
        self.cor = cor
    
    def destampar(self):
        try:
            self.tampa = False
        except:
            print("A caneta já está sem tampa!")

    def tampar(self):
        try:
            self.tampa = True
        except:
            print("A caneta ainda está tampada!")

    def escrever(self , mensagem):
        if self.tampa == True:
            print("Retire a tampa para escrever")
        
        else:
            print(f"[{self.cor}]{mensagem}[/]")

c1 = Caneta("red")
c1.destampar()
c1.escrever("teste monstro cachorro")
c1.tampar()
c1.escrever("testando")