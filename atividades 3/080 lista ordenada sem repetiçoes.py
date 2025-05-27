lista = []
pos = 0

for cont in range (0,5): #esse loop vai girar 5 vezes
    valor = int(input('digite um valor: ')) #input pro usuario digitar o valor
    if valor in lista: #se o valor estiver na lista, a mensagem aparece pedindo um valor novo
        print('digite um novo valor, esse já existe')
    elif cont == 0 or valor > lista[-1]: #se o valor for  primeiro digitado maior que o ultimo, o valor é adicionado no final da lista
        lista.append(valor) #adiciona o valor ao fim da lista
        print('valor adicionado na ultima posição')
    else: #se nao corresponde a nenhuma condição acima, entra no loop
        while True:
            if valor < lista[pos]: #se o valor for menor que o valor na posição "pos" ele é inserido nessa posiçao
                lista.insert(pos, valor) #insere o valor na posiçao pos
                print(f'valor adicionado na posição: {pos}')
                break #quando o valor for inserido ele sai do loop
            pos += 1 #se não sair do loop o valor, a variavel pos soma 1
print(f'a lista ordenada fica: {lista}') #exibe a lista ordenada