import random

n1 = input('vamos fazer um sorteio? digite 4 nomes para começar:')
n2 = input('mais uma vez: ')
n3 = input('de novo: ')
n4 = input('ultima vez: ')

sorte = random.choice ([n1, n2, n3, n4])

print (f'e o ganhador desse sorteio foi ..... 👀 \n \n {sorte}, parabéns!!!!!!')
