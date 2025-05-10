numeros = []
for c in range (0, 5):
    valores = int(input('digite um numero: '))
    for itens in valores:
        if valores < numeros:
            numeros.insert(itens-1,valores)
        else:
            numeros.append(itens,valores)
