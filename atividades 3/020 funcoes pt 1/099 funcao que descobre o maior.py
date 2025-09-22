from time import sleep
def calculadora(*num):
    print( '=-' * 20)
    print('analisando valores...')
    sleep(0.5)
    for p, v in enumerate(num):
        print(v, end=" ")
        sleep(0.5)
    print(f'foram informados {len(num)} valores ao todo.')
    print(f'o maior valor informado foi: {max(num)}')

calculadora(1, 2, 3, 4, 5, 6)
calculadora(4, 7, 0)
calculadora(0)
calculadora(6)
print("\n","\n")