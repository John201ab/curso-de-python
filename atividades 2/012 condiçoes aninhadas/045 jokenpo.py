from random import randint
from time import sleep
computador = randint(0,2)
print('-=' * 2 + 'jokenpo' + '-=' * 2)
sleep(1)
print('e ai? vamos jogar?')
sleep(2)
jogador = int(input('''[0]Pedra
[1]Papel
[2]Tesoura
escolha uma das opçoes:'''))

if jogador < 0 or jogador > 2 :
    print('jogada invalida!!')

else:
    print('vamos lá?')
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')
    sleep(1)
    lista = ('Pedra','Papel','Tesoura')
    print(f'''computador:{lista[computador]}
jogador:{lista[jogador]}''')
    if jogador < 0 or jogador > 2 :
        print('jogada invalida!!')

    elif jogador == 0:
        if computador == 0:
            print('EMPATE!')
        elif computador == 1:
            print('VOCÊ PERDEU!!')
        elif computador == 2:
            print('VOCÊ VENCEU!!')

    elif jogador == 1:
        if computador == 0:
            print('VOCÊ VENCEU!!')
        elif computador == 1:
            print('EMPATE!!')
        elif computador == 2:
            print('VOCÊ PERDEU!!')

    elif jogador == 2:
        if computador == 0:
            print('VOCÊ PERDEU!!')
        elif computador == 1:
            print('VOCÊ VENCEU!!')
        elif computador == 2:
            print('EMPATE!!')

