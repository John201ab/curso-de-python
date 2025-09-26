def conversor(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('Erro! digite um numero válido')
        else:
            valido = True
            return float(entrada)
