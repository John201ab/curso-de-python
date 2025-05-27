lista = []
cont = cinco = 0
escolha = 'S'
while escolha == 'S':
    valor = int(input('digite um valor:'))
    escolha = input('você quer continuar? [S/N]').upper()
    if valor == '5':
        cinco += 1
    if escolha == 'nN':
        break
    elif escolha not in 'SsNn':
        print('nao entendi, responda apenas com S ou N')
        while escolha2 != 'SsNn':
            escolha2 = input('quer continuar? [S/N]')
            
    cont += 1
listaNova = sorted(lista, reverse = True)
print(f'foram digitados {cont} numeros.'
      'a lista organizada de forma decrescente ficoiu:{listaNova}')

if '5' in lista:
    print('ah, ja ia esquecendo; o numero 5 está na lista, e foi digitado {cincos} vezes')
else:
    print('ah, ja ia esquecendo; cinco não está na lista')