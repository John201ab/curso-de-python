def metade (numero, form = False):
    if form == True:
        met = numero / 2
        numero = moeda(met)
        return numero 

    else:
        met = numero / 2
    return met
  
    
def dobro(numero, form = False):
    if form == True:
        met = numero / 2
        numero = moeda(met)
        return numero 

    else:
        met = numero * 2
        return met

def aumentado(numero, form = False):
    if form == True:
        aum = numero / 2
        numero = moeda(aum)
        return numero 

    else:
        aum = numero / 2
    return aum

def reduzido(numero, form = False):
    if form == True:
        red = numero / 2
        numero = moeda(red)
        return numero 

    else:
        red = numero / 2
        return red

def moeda(valor):
    numero = f'R$ {valor:,.2f}'.replace(',', 'x').replace('.', ',').replace('x','. ')
    return numero