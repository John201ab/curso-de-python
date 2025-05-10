numero = int(input('digite um numero:' ))
numero2 = int(input('agora outro: '))
numero3 = int(input('só mais um: '))

if numero > numero2 and numero > numero3:
    print(f'{numero} é maior que: {numero2} e {numero3}')

elif numero2 > numero and numero2 > numero3:
    print(f'{numero2} é maior que {numero} e {numero3}')

elif numero3 > numero2 and numero3 > numero:
    print(f'{numero3} é maior que {numero2} e {numero}')

else:
    print('todos os numeros tem o mesmo valor')