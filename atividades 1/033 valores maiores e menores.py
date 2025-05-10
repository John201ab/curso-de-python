numero = (input('digite três numeros e eu mostrarei qual o menor e o maior: '))
num0 = int(numero[0])
num1 = int(numero[1])
num2 = int(numero[2])
if num0 > num1 and num0 > num2:

    print(f'o numero {num0} é maior que {num1} e {num2}')

elif num1 > num0 and num1 > num2:
    print(f'o numero {num1} é maior que {num0} e {num2}')

else:
    print(f'o numero {num2} é maior que {num0} e {num1}')

#pósaula corrigido e completo
a = input('digite um numero: ')
b = input('agora outro: ')
c = input('só mai suma vez: ')

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print(f' o maior numero é: {maior}e o e menor{menor}.')