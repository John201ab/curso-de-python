def metade (numero):
    met = numero / 2
    return met

def dobro(numero):
    dob = numero * 2
    return dob

def aumentado(numero, valor = 0):
    aument = numero + (numero * valor / 100)
    return aument

def reduzido(numero, valor = 0):
    reduz = numero - (numero * valor / 100)
    return reduz


def moeda(valor):
    numero = f'R$ {valor:,.2f}'.replace(',', 'x').replace('.', ',').replace('x','. ')
    return numero