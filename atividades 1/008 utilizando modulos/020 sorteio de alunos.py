import random

print('você é um professor e vai sortear a ordem de apresentaçao de um trabalho, quais alunos vão apresentar?')

n1 = input('digite um nome: ')
n2 = input ('agora outro: ')
n3 = input ('mais um: ')
n4 = input ('agora o último: ')

nome = [n1, n2, n3,n4]

random.shuffle(nome)

print (f'agora vamos sortear a ordem de apresentação dos trabalho, e a ordem é: {nome}')