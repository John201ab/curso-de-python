import random
numero = random.randint(0,5)
print('estou pensando em um numero, você consegue adivinhar?')
escolha = (input('escolha um numero entre 0 e 5: ')).strip()
if  numero == escolha:
    print('PARABENS, VOCÊ ACERTOU!!!')
elif escolha >= '6':
    print('essa é uma opçao invalida, tente novamente mais tarde')
else:
    print(f'você errou, o numero escolhido foi: {numero}')
