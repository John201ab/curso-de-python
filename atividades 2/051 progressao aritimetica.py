print('''sabe como funciona a progressao aritimetica? vc escolhe um numero e um intervalo entre eles
e eu conto os primeiros 10 numeros dessa progressao''')

termo = int(input('entao escolha o termo: '))
razao = int(input('agora a razão: '))

for c in range(termo, termo + 10 * razao, razao):
    print(c, end= ' >> ')
print('fim')