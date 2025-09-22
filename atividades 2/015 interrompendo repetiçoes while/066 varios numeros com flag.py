flag = soma = 0 #flag e soma recebem o mesmo valor
while True: #enquanto for verdadeiro vai ficar em looping
    flag = int(input('digite um numero, mero mortal: '))
    if flag == 999: #se o usuario digitar 999
        break #o programa para
    else: #se nao
        soma += flag #soma vai somar o valor do flag a cada volta do looping
print(f'a soma de tudo deu: {soma}!') #no final, o valor de soma