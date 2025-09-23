def resumo(numero, aumento = 0, redução = 0):    

    valor = moeda(numero)
    dobro = moeda(numero*2)
    metade = moeda(numero/2)
    aumen = moeda(numero + (numero * 80) / 100)
    reduc = moeda((numero * redução) / 100)
    tabela = (f'''
{linha()}
{f'RESUMO DO VALOR':^40}
{linha()}
preço analisado:{valor:.>20}
dobro do preço:{dobro:.>22}
metade do preço:{metade:.>20}
80% de aumento:{aumen:.>20}
35% de redução:{reduc:.>20}
{linha()}''')

    print(tabela)


def moeda(valor):
    numero = f'R$ {valor:,.2f}'.replace(',', 'x').replace('.', ',').replace('x','. ')
    return numero

def linha():
    return('-' * 40)