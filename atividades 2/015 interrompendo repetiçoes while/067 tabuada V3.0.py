print('=-' * 20)
print(f'{'tabuada do john V3.0':^40}')#titulo bonitinho
print('=-' * 20)
while True: #enquanto for verdadeiro seguirá esse loop
    valor = int(input(' quer ver a tabuada de qual valor? '))
    if valor > 0: #se valor for maior que 0
        for c in range (1, 11): #vai acontecer um looping de 0 a 10
            print(f'{valor} X {c} = {valor * c}')
        print('=-' * 20)
    elif valor <= 0: # se for menor ou igual a 0 o programa para
        print('programa encerrado, obrigado e volte sempre!')
        break