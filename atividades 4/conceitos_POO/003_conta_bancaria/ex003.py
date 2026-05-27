from rich import inspect

class ContaBancaria:
    """
    Cria uma conta bacária que permite fazer saques e depósitos 
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com um saldo de R${self.saldo:,.2f}")

    def __str__(self):
        return  f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo"
    
    def depositar(self , valor):
        self.saldo += valor
        print(f"Depósito de R${valor:,.2f} efetuado com sucesso!")

    def sacar(self, valor):
        self.saldo -= valor
        print(f"saque de R${valor:,.2f} efetuado com sucesso!")

    
c1 = ContaBancaria(1, "João", 5000)
c1.depositar(500)
c1.sacar(700)
inspect(c1)
inspect(ContaBancaria)