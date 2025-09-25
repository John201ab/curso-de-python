def leiaDinheiro(msg, aumento = 0, redução = 0):
    validador = msg
    if validador.isnumeric():
        conversao = int(msg)
        valor = resumo(conversao, aumento, redução)
        return(valor)

    else:
        while True:
            if validador.isnumeric():
                conversao = int(validador)
                break
            else:
                validador = input('digite um valor válido: ')
        valor = resumo(conversao, aumento, redução)

def resumo(numero, aumento , redução):    

    valor = moeda(numero)
    dobro = moeda(numero*2)
    metade = moeda(numero/2)
    aumen = moeda(numero + (numero * aumento) / 100)
    reduc = moeda((numero * redução) / 100)
    tabela = (f'''
{linha()}
{f'RESUMO DO VALOR':^40}
{linha()}
preço analisado:{valor:.>20}
dobro do preço:{dobro:.>22}
metade do preço:{metade:.>20}
{aumento}% de aumento:{aumen:.>20}
{redução}% de redução:{reduc:.>20}
{linha()}''')

    print(tabela)


def moeda(valor):
    numero = (f'R$ {valor:,.2f}').replace(',', 'x').replace('.', ',').replace('x','. ')
    return numero

def linha():
    return('-' * 40)