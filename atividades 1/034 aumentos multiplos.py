salario = float(input('digite o valor do salario para calcularmos o aumento: '))

a = 10
b = 15

aumento1 = salario  + (salario * 10 / 100)
aumento2 = salario + (salario * 10 / 100)


if salario > 1250.00:
    print (f"o valor do aumento de salario será de {b}%, saindo de {salario} para {aumento2:.2f}")

else:
    print (f"o valor do aumento será de {a}%, saindo de {salario} para {aumento1:.2f}")