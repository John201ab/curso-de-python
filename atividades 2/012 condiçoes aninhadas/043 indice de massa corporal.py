peso = float(input('digite o seu peso'))
altura = float(input('digite sua altura'))

imc = peso / (altura * 2)

if imc < 18.5:
    print(f'{imc:.2f}abaixo do peso ideal')

elif imc > 18.5 and imc < 26:
    print(f'{imc:.2f}peso ideal')

elif imc > 25 and imc < 31:
    print(f'{imc:.2f}sobrepeso')

elif imc > 30 and imc < 41:
    print(f'{imc:.2f}obesidade')

else:
    print(f'{imc:.2f}obesidade morbida')
