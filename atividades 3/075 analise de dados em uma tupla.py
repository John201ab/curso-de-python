valor1 = int(input('digite um valor: '))
valor2 = int(input('digite outro valor: '))
valor3 = int(input('digite mais um valor: '))
valor4 = int(input('digite um ultimo valor: '))
tuplinha = (valor1, valor2, valor3, valor4) #coloca todos os valores dentro da tupla
cont9 = 0 #contador de 9
cont3 = pares = mensagem = () #contador de 3, pares e mensagem

for cont in tuplinha: #leia toda tuplinha
    if cont == 9: #se 9 estiver em tuplinha
        cont9 += 1 #contador do 9 recebe + 1

for cont in tuplinha: #leia toda tuplinha
    if cont == 3: #se cont for igual a 3
        cont3 = (tuplinha.index(3)) #contador de 3 recebe +1
        mensagem = f'o valor 3 apareceu na {cont3}º posiçao'
    else: #se nao, mensagem de 'erro'
        mensagem = '3 nao aparece em nenhuma posiçao'

for cont in tuplinha: #leia toda tuplinha
    if cont % 2 == 0: #se o resto da divizao de 2 der 0
        pares += cont, #contador de pares recebe +1

print(f'''Voce digitou os valores: {tuplinha}
o valor 9 apareceu {cont9} vezes
{mensagem}
e dos valores digitados, os numeros: {pares} sao pares.''')
print(f'{tuplinha.count(9)}')
print(tuplinha.index(3))