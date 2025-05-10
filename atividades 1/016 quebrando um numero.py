from math import trunc#, floor
num = float(input('digite um numero real' ))               #tbm da pra usar int
print(f'o numero escolhido foi: {num}, ele arredondado é: {trunc(num)}')

#feito com ajuda de chat gpt pra entender o uso de if e else

#isola o numero decimal
#parte_decimal = num - floor(num)

#se for maior que 0.5 arredonda pra cima
#if parte_decimal >=0.5: numero_inteiro = ceil(num)

#caso contrario, pra baixo
#else: numero_inteiro = floor (num)