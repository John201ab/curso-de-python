from random import randint
valores = tuple(randint(0,10) for c in range (5)) #coloca 5 valores aleatorios na tupla
organizado = sorted(valores) #organiza em ordem crescente
print(f'os valores são: {valores}.\n o maior é {organizado[-1]} e o menor {organizado[0]}')