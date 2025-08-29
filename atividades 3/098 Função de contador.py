from time import sleep

def contador():
    
for contador in range(1, 11):
    print(contador, end=' ')
    sleep(0.5)
print('\n')
for contador2 in range(10, 0, -1):
    print(contador2, end=' ')
    sleep(0.5)

inicio = input('Digite um numero inicial: ')
fim = input('Digite o numero final: ')
salt = input('Pulando de quanto em quanto? ')

