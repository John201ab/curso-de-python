d = int(input('você alugou o carro por quantos dias? '))
km = float(input('rodou por quantos km? '))
vd = 60 * d
vkm = 0.15 * km
r = vd + vkm
print (f'sabendo que o valor por dia é 60R$ e 0,15R$ o km, o valor  da diaria é: {vd}, dos km`s são: {vkm:.2f} \n '
       f'entao o total a ser pago é: {r}')
