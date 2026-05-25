#Declaração de Classe

class Gafanhoto:
    def __init__(self, nome = "", idade = 0):  #metodo construtor
        #Atributos de intancia
        self.nome = nome
        self.idade = idade
        

    #Métodos de instancia
    def aniversário(self):
        self.idade += 1

    def __str__(self):
        return f"Olá {self.nome}, você tem {self.idade} anos de idade"
    
    def __getstate__(self):
        return f"Estado: nome  = {self.nome}, idade = {self.idade}"
#declaração de Objetos
g1 = Gafanhoto("Julia", 15)
print(g1)
print(g1.__dict__) #atributo

print("=+" * 10)
g2 = Gafanhoto("João", 21)
print(g2)
print(g2.__getstate__()) #método
print(g2.__class__)


    #print(g1.__doc__) #Dunder Attribute