lista = []
pos = 0

for cont in range (0,5):
    valor = int(input('digite um valor: '))
    if valor in lista:
        print('digite um novo valor, esse já existe')
    elif cont == 0 or valor > lista[-1]:
        lista.append(valor)
        print('valor adicionado na ultima posição')
    else:
        while True:
            if valor < lista[pos]:
                lista.insert(pos, valor)
                print(f'valor adicionado na posição: {pos}')
                break
            pos += 1
print(f'a lista ordenada fica: {lista}')