while True:
    print(15 * '=-')
    print('analisando triangulos')
    print(15 * '=-')

    ang1 = int(input('digite o valor de um angulo: '))
    ang2 = int(input('digite o valor de outro angulo: '))
    ang3 = int (input('digite mais um: '))

    if ang1 + ang2 > ang3 and ang2 + ang3 > ang1 and ang3 + ang1 > ang2:
        if ang1 == ang2 == ang3:
            print('seu triangulo é um equilatero')

        elif ang1 == ang2 and ang2 == ang3 and ang1 == ang3:
            print('seu tringulo é um isósceles')

        else:
            print('seu triangulo é um escaleno')

    else:
        print('seus valores nao formam um triangulo')

    continuar = input('\nAperte "enter" para inserir novos valores ou digite "sair" para sair').strip()

    if continuar.lower() == 'sair':
        break

