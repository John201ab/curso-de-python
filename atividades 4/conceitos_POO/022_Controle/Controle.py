from rich.traceback import install

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
        if cmd == ">":
            if self.canal < 5:
                self.canal +=1 
            else:
                self.canal = 0
            print(self.canal)
        if cmd == "<":
            if self.canal >= 2:
                self.canal -= 1
                print(self.canal)
            else:
                self.canal = 5
                print(self.canal)

    def aumentar(self, cmd):
        if cmd == "+":
            if self.volume < 5:
                self.volume += 1
                print(self.volume)
        if cmd == "-":
            if self.volume >= 2:
                self.volume -= 1
                print(self.volume)   
        else:
            print(self.volume)   

c1 = Controle()        

while True:
    cmd = input('teste')

    c1.comando(cmd)
