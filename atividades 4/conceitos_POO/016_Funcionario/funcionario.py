from rich import print
from rich.traceback import install
from rich import inspect
install()

class Funcionario():
    def __init__(self, nome, funcao, setor):
        #Atributos de instancia
        self.nome = nome
        self.funcao = funcao
        self.setor = setor

    def __repr__(self):
        return f"Olá, me chamo {self.nome!r}! Sou {self.funcao!r} na equipe de {self.setor!r}"
    
f1 = Funcionario( "joão", "analista", "suporte")
inspect(f1)
print(f1)
f2 = Funcionario(  "Rubens", "analista", "Redes")
inspect(f2)
print(f2)