print('''sabe como funciona a progressao aritimetica? vc escolhe um numero e um intervalo entre eles
e eu conto os primeiros 10 numeros dessa progressao''')
termo = int(input('digite o termo a ser usado: '))
razao = int(input('agora a razao: '))
contador = 0
while contador < 10:
    print(termo, ' > ', end = '')
    termo += razao
    contador += 1
