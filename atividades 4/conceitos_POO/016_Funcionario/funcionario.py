from rich import print
from rich.traceback import install

install()

class Funcionario():
    def __init__(self, nome, funcao, setor):
        self.nome = nome
        self.funcao = funcao
        self.setor = setor

    def __repr__(self):
        return f"Olá, me chamo {self.nome!r}! Sou {self.cargo!r} na equipe de {self.setor!r}"
    
f1 = Funcionario( "joão", "analista", "suporte")

f2 = Funcionario(  "Rubens", "analista", "Redes")

print(f1)
print(f2)