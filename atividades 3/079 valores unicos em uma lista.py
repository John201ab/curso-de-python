lista = []
flag = "S" #flag passa a ser: "S"
while flag == 'S': #enquanto flag for "S" todo o aninhamento ficará em loop
    valor = int(input('digite um valor, meu nobre: ')) #o usuario digita o valor
    while valor in lista: #enquanto o usuario digitar um valor que está na lista, esse aninhamento fica em loop
        valor = int(input(f'valor {valor} ja cadastrado, tente outro: ')) #mensagem de erro e petiçao pra um novo valor
        if valor not in lista: #se o novo valor nao estiver na lista:
            print('agora sim, valor cadastrado com sucesso!!') #mensagem de confirmação
            lista += valor, #lista recebe mais esse item
            break #o primeiro loop para
    else: #se o usuario digitar um numero que não está na lista: 
        lista += valor, #lista recebe o valor
        print('valor adicionado com sucesso!!') #mensagem de confirmação

    flag = input('deseja continuar? [s/n]: ').upper() #o usuario altera a flag e decide se quer continuar
    if flag == ['N','n']: #se flag for igual a : 'n', o programa para
        break
    if flag not in ['S','s','N','n']: #se o usuario digitar algo diferente de 's' ou 'n':
        while flag not in ['S','s','N','n']: #entra no loop até digitar certo
         flag = input('nao entendi, digite [S/N]')
lista1 = lista.sort() #organia a lista em ordem crescente
print(f'foram digitados os valores: {lista}')