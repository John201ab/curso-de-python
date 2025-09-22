sexo = str(input('digite seu sexo[M/F]: ')).upper()[0].strip() #o usuario digita
while sexo not in 'MF': #enquanto sexo nao for M ou F
    sexo = str(input('opçao invalida, por favor, informe seu sexo com: ''F'' ou ''M''')).upper()[0] #sexo recebe a nova mensagem

print(f' a opçao escolhida foi: {sexo}') #print mostrando o resultado


