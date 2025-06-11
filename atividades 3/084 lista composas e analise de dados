pessoas = []
pessoamin = []
pessoamax = []
contador =  0
print('/'* 30)
while True:   #enquanto o usuario nao digitar 'n' o loop continua
    pessoas.append(str(input('digite seu nome: '))) #adiciona o nome a lista 'pessoas'
    pessoas.append(int(input('digite seu peso: '))) #adiciona o peso, fazendo a lista ter dois itens 
    escolha = input('quer continuar? [S/N]').upper() #o quebra loop
    print('/'* 30)
    if pessoamax == [] : #se pessoamax for uma lista vazia, essa lista e pessoamin receberao o valor de pessoas
        pessoamax = (pessoas)
        pessoamin = (pessoas)
    elif pessoas[1] > pessoamax[1]: #se o item na posiçao 1 de pessoas, noo caso o peso, for maior q a de pessoa max
      pessoamax = pessoas #pessoamax substitui o valor da lista pelo novo valor
    elif pessoas[1] < pessoamin[1]: #nesse caso, ele checa se o valor é menor e faz o mesmo de cima
        pessoamin = pessoas
    pessoas = [] #os valores ja foram checados, entao a lista vai resetar pra começar tudo dnv
    contador += 1 #o contador recebe + 1 pra exibir quantas pessoas foram cadastradas ao todo
    if escolha == 'N': #se escolha for 'N' o loop breca
        break
print('=-' * 30)
print(f'foram cadastradas {contador} pessoas')
print(f'''a pessoa mais pesada é {pessoamax[0]} e pesa: {pessoamax[1]}. 
e a mais leve é {pessoamin[0]} pesando {pessoamin[1]}''') 
print('=-' * 30)
