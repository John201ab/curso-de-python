total = 0
numero = int(input('digite um numero:'))
for c in range(1, numero +  1):
    if numero % c == 0 :
        total += 1
        print('\033[33m', end = ' ')
    else:
        print('\033[31m', end = ' ')
    print(c, end = ' ')
if total == 2:
    print(f'\033[97m \n o numero {numero} é primo, foi dividido {total} vezes')
else:
    print(f'\033[97m \n numero {numero} nao é primo, foi dividido {total} vezes')
