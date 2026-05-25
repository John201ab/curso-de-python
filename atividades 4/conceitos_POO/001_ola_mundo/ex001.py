#Declaração de Classe

class Gafanhoto:
    def __init__(self):  #metodo construtor
        #Atributos de intancia
        self.nome = "pessoa"
        self.idade = 0
        

    #Métodos de instancia
    def aniversário(self):
        self.idade += 1

    def mensagem(self):
        return f"Olá {self.nome}, você tem {self.idade} anos de idade"
    
#declaração de Objetos
g1 = Gafanhoto()
print(g1.mensagem())

print("=+" * 10)
g2 = Gafanhoto()

g2.idade = 21
g2.nome = "joao"
print(g2.mensagem())


    