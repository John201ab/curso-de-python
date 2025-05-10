#provavelmente é uma gambiarra violenta q vou rir muito no futuro (espero

valor_do_saque = int(input('Digite um valor a ser sacado: R$')) #input do valor
saque = cinquenta = vinte = dez = cinco = um = 0 #variaveis
while saque != valor_do_saque: #enquanto a soma for diferente do valor do usuario, o programa vai rodar
    while True: #enquanto for verdadeiro ficaem loop
        if saque + 50 > valor_do_saque: #se o valor da soma + 50 for maior q o do usuario
            break #quebra o loop e passa pro proximo
        else: #se nao
            saque += 50 #soma recebe + 50
            cinquenta += 1 #contador de notas recebe +1
    #a partit daqui tudo se rebete mas referente a cada cedula de valor especifico
    while True:
        if saque + 20 > valor_do_saque:
            break
        else:
            saque += 20
            vinte += 1
    while True:
        if saque + 10 > valor_do_saque:
            break
        else:
            saque += 10
            dez += 1
    while True:
        if saque + 5 > valor_do_saque:
            break
        else:
            saque += 5
            cinco += 1
    while True:
        if saque + 1 > valor_do_saque:
            break
        else:
            saque += 1
            um += 1
print(f''' o valor sacado foi: {valor_do_saque}, e foram usadas {cinquenta} notas de 50, {vinte} de 20, {dez} de 10,
{cinco} de 5 e {um} de 1. Obrigado e  volte sempre!!!''') #print das somas


