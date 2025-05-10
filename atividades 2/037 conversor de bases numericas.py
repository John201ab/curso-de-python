numero = int(input('digite um numero inteiro: '))
conv = int(input('''escolha uma opção
[1] Binario
[2] Octadecimal
[3] Hexadecimal
o que você escolhe? '''))

if conv< 1 or conv > 3:
     print('escolha invalida')

else:
     if conv == 1:
          print(f'o valor:{numero} convertido pra binario é: {bin(numero)[2:]}')

     elif conv == 2:
          print(f'o valor:{numero} convertido para octagonal é: {oct(numero)[2:]}')

     elif conv == 3:
          print(f'o valor: {numero} convertido para hexagonal é {hex(numero)[2:]}')