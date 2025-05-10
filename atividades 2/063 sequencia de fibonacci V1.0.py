numero = int(input('digite a quantidade de valores q aparecerao nessa sequencia: '))
sucessor = 1
atual = 0
contador = 1
print('0', end =' ')
while contador < numero:
     soma = atual + sucessor
     atual = sucessor
     sucessor = soma
     contador += 1
     print(f' -> {atual}', end = '')
