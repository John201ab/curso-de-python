from time import sleep
# função que faz contagem de x até y pulando de z em z
def contador(a, b, c):
    for numero in range(a + 1, b + 1, c):
        print( numero, end= " ")
        sleep(0.5)
    print('Fim!')
for contador in range(1, 11):
    print(contador, end=' ')
    sleep(0.5)
print('\n')
for contador2 in range(10, 0, -1):
    print(contador2, end=' ')
    sleep(0.5)
print("\n")
inicio = int(input('Digite um numero inicial: '))
fim = int(input('Digite o numero final: '))
salt = int(input('Pulando de quanto em quanto? '))
if salt == 0:
    salt = 1

if fim < inicio:
    salt = -abs(salt)
    inicio = inicio - 1
    fim = fim - 1

# define os valores para a contagem personalizada
contador(inicio, fim, salt)
