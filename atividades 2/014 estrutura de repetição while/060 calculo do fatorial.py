numero = int(input('digite o seu numero'))
resultado = 1
print(f'calculando {numero}!')
print(numero, end = "")
while numero != 1:
    resultado *= numero
    numero = numero-1
    print(' x', numero, end = '')
print(' = ', resultado)