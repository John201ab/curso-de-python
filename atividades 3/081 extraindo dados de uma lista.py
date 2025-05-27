lista = []
cont = cinco = 0  #variaveis
escolha = 'S'

while escolha == 'S': #enquanto escolha for igual a "S" o loop fica rodando
    valor = int(input('digite um valor: ')) #input do usuario
    escolha = input('você quer continuar? [S/N]: ').upper() #validaçao pro loop continuar rodando, caso seja n o loop para
    if valor == 5: #se o valor digitado for igual a 5
        cinco += 1 # a variavel cinco soma 1
    if escolha == 'nN': #se a escolha for "N" o loop para
        break #isso para o loop
    while escolha not in ['S','N']: #caso o valor da escolha seja diferente de "S ou N" o loop vai ficar rodando
        escolha = input('nao entendi, quer continuar? [S/N]').upper()

    cont += 1 #cada vez q o loop girar o contador soma 1 pra mostrar no final quantos numeros foram adicionados na lista
    lista += [valor]#lista recebe o valor digitado pelo usuario
listaNova = sorted(lista, reverse = True) #ao final do loop ele organiza a lista em ordem decrescente

print(f'foram digitados {cont} numeros. \n'
      f'a lista organizada de forma decrescente ficou:{listaNova}') #mostra quantos numeros foram inseridos e a ordem

if 5 in lista: #se o "5" estiver na lista, ele fala quantas vezes aparece
    print(f'ah, ja ia esquecendo; o numero 5 está na lista, e foi digitado {cinco} vezes')
else: #caso contrario mostra uma mensagem de que nao achou
    print('ah, ja ia esquecendo; cinco não está na lista')