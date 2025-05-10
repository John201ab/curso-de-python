from random import randint
print('=-' * 20)
print(f'{'vamos jogar PAR ou IMPAR':^40}') #titulo bonitinho
print('=-' * 20)

contjog = 0 #contador do jogador

while True:
    computador = randint(0, 10)  # computador escolhe um numero
    valor = int(input('digite um valor: ')) #jogador escolhe um numero
    escolha = str(input('Par ou Impar? [P/I]: ')).upper().strip()[0] #jogador escolhe impar ou par
    soma = (computador + valor)   # soma dos valores e divisao pra saber se é par ou nao
    resultado = soma % 2 #verificaçao do impar ou par
    print(f'você escolheu {valor} e a maquina {computador} somando {soma}.')
    if  escolha == 'P' and resultado == 0: #verificaçao de vitoria se a escolha for par
        print('o numero é PAR, você ganhou')
        contjog += 1
        print('=-' * 20)
    elif escolha == 'I' and resultado != 0: #verificaçao de vitoria se a escolha for impar
        print('o numero é Impar, você ganhou')
        contjog += 1
        print('=-' * 20)
    elif escolha == 'P' and resultado != 0 or escolha == 'I' and resultado == 0: #verificaçao de perda
        print(f'YOU LOSE!!!! \n Você venceu {contjog} vezes.')
        break
print('=-' * 20)
