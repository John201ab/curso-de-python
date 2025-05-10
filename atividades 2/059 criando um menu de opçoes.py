from time import sleep  #importando biblioteca
flag = '' #variavel q controla tudo
print('=-' * 20)
valor1 = int(input('digite um valor: ')) #entrada do primeiro valor
valor2 = int(input('digite um segundo valor')) #entrada do segundo
while flag != 5: #enquanto flag for diferente de 5
    flag = (int(input('''    [1]somar 
    [2]multiplicar
    [3]maior
    [4]novos numeros
    [5]sair \n
o que você quer fazer? '''))) #menu pro usuario
    if flag == 1: #se escolher 1, o programa soma
        result = valor1 + valor2
        print(f'o resultado da soma deu: {result}')
        print('=-' * 20)
    if flag == 2: #se escolher 2, multiplica
        result = valor1 * valor2
        print(f'o resultado da multiplicaçao deu: {result}')
        print('=-' * 20)
    if flag == 3: #3 define maior e menor
        if valor1 > valor2:
            print(f'o maior valor é: {valor1}')
            print('=-' * 20)
        elif valor1 == valor2:
            print(' os valores sao iguais')
            print('=-' * 20)
        else:
            print(f'o resultado do maior valor é: {valor2}')
            print('=-' * 20)
    if flag == 4: #opçao para digitar novos numeros
        print('=-' * 20)
        valor1 = int(input('digite um novo numero: '))
        valor2 = int(input('mais um: '))
    if flag not in (1,2,3,4,5): #casoo usuario escolha uma opçao invalida
        flag = int(input('opçao invalida, tente novamente'))
print('fechando programa...') #assim q o usuario digitar 5 aparece essa animaçao de fechamento
sleep(3)
print('programa finalizado')
