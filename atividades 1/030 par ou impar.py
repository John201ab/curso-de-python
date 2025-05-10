numero = input(' digite um numero, vou dizer se ele é par ou impar: ')
valor = int(numero[-1])
if valor in [2,4,6, 8] :
    print(f'{numero} é par')

else:
    print(f'{numero} é impar')