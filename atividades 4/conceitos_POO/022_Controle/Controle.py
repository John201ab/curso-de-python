from rich.traceback import install
from rich.panel import Panel
from rich import print

install()



class Controle():

    ligado = False
    canal = 1
    volume = 2

    def comando(self,cmd):
        if cmd == "@":
            self.ligar()

        if cmd == ">" or cmd == "<":
            self.passar(cmd)
            
        if cmd == "+" or cmd == "-":
            self.aumentar(cmd)

    def ligar(self):
        if self.ligado == False:
            self.ligado = True
            print("A tv stá ligada!")
        else:
            self.ligado = False
            print("A tv está desligada!")
            
    
    def passar(self, cmd):

        if cmd == ">" and self.ligado == True:
            if self.canal < 5:
                self.canal +=1 
            else:
                self.canal = 0
            print(self.canal)
        elif cmd == "<" and self.ligado == True:
            if self.canal >= 2:
                self.canal -= 1
                print(self.canal)
            else:
                self.canal = 5
                print(self.canal)
        else:
            print(Panel("A tv está desligada", title="[ tv ]"))

    def aumentar(self, cmd):
        try:
            if cmd == "+" and self.ligado == True:
                if self.volume < 5:
                    self.volume += 1

                print(Panel("CHANNEL = 1 2 3 4 5 \nVOLUME = ", title="[ tv ]")) 
                
            if cmd == "-" and self.ligado == True:
                if self.volume >= 2:
                    self.volume -= 1

                print(self.volume)   
        
        except:
            print("A televisão está desligada")

c1 = Controle()        

while True:
    cmd = input('< CH >  - VOL +')

    c1.comando(cmd)
