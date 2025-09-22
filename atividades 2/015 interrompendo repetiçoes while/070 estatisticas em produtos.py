titulo = "john's store"
print(titulo.center(40, '='))

escolha = nome = nome_mais_barato = '' #variaves str
total = mais_de_mil =  mais_barato = cont = 0 #variaveis int
while escolha in 'Ss': #enquanto escolha for s
    nome = str(input('Qual o nome do produto?'))
    preco = float(input('Qual o valor do produto? R$ '))
    total += preco
    cont += 1
    if cont == 1: #se for o primeiro item digitado, mais barato recebe preco
        mais_barato = preco; nome_mais_barato = nome
    if preco < mais_barato: #se o novo valor for menor q mais barato, mais barato recebe esse valor
        mais_barato =  preco; nome_mais_barato = nome
    if preco > 999: # se preço for maior que mil, a variavel recebe mais 1
        mais_de_mil += 1
    if preco < mais_barato: #se preço for menor que mais barato
        mais_barato = preco #mais barato recebe preco
        nome_mais_barato = nome #nome mais barato recebenome
    escolha = str(input('Quer continuar? [S/N]')).strip()[0] #opçao pro usuario continuar
print('-' * 40)
print(f'''O total da compra foi: {total:.2f}
Temos {mais_de_mil} produtos custando mais de 1k
O produto mais barato foi: {nome_mais_barato} custando {mais_barato:.2f} R$''')