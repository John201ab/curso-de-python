lista = []
while flag == 'Ss':
    valor = int(input('digite um valor, meu nobre: '))
    if valor in lista:
        valor = int(input(f'valor {valor} ja cadastrado, tente outro: '))
    else:
        lista += valor,

    flag = input('deseja continuar? [s/n]: ')
    if flag == 'Nn':
        break
    if flag != 'SsNn':
        flag = input('digite [S/N]')
