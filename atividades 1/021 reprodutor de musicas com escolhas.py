import pygame
pygame.init()
escolha = (str(input('qual vc prefere? ir para a selva? ou bater nas portas para o Céu?: '))
           .strip().lower().replace('céu', 'ceu'))

if escolha == 'selva':
    pygame.mixer.music.load ('atividades 1/jungle.mp3')
    print('bem vindo a selva baby')

elif escolha  == 'ceu':
    pygame.mixer.music.load ('atividades 1/heaven.mp3')
    print('batamos nas portas do céu')

else:
    print('opçao invalida, nenhuma  musica será tocada')
    exit()

pygame.mixer.music.play()

input('precione enter para encerrar...')
pygame.event.wait()