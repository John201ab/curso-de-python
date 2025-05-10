from random import randint #imoporta a biblioteca de numeros aleatorios
computador = randint(0,10) #computador escolhe de 0 a 10
contador = 1 #contador de tentativas
print('vou pensar em um numero, será que voce consegue acertar?')
escolha = int(input('digite um numero  de 0 até 10: ')) #variavel que recebe o cute do jogador
while escolha != computador: #enquanto a escolha for diferente do q o computador escolheu
    if escolha > computador: #se escolha for maior q computador
        print('menos...')
    elif escolha < computador:#se escolha for maior2
        print('mais..')
    escolha = int(input('escolha errada, tente de novo')) #variavel continua perguntando

    contador +=  1 #contador acumula os erros
print(f'PARABENS, depois de tentar {contador} vezes, vc finalmente adivinhou que o numero era: {computador}')
