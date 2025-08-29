from time import sleep
def calculadora(tupla):
    print( '=-' * 20)
    print('analisando valores...')
    sleep(0.5)
    for p, v in enumerate(tupla):
        print(v, end=" ")
        sleep(0.5)
    print(f'foram informados {len(tupla)} valores ao todo.')
    print(f'o maior valor informado foi: {max(tupla)}')

numeros = [1, 2, 3, 4, 5, 6]
calculadora(numeros)
numeros = [4, 7, 0]
calculadora(numeros)
numeros = [0]
calculadora(numeros)
numeros = [6]
calculadora(numeros)
print("\n","\n")