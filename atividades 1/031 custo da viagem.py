viagem = float(input('qual a distancia em km da sua viagem?'))
if viagem <= 200:
    valor1 = 0.50 * viagem
    print(f'o valor da sua viagem é: {valor1}')

else:
    valor2 = 0.45 * viagem
    print(f'o valor da sua viage é {valor2}')