from time import sleep
# função que faz contagem de x até y pulando de z em z
def contador(a, b, c):
    for numero in range(a + 1, b + 1, c):
        print( numero, end= " ", flush = True)
        sleep(0.5)
    print('Fim!')

#contador de 0 a 10
for numeros in range(1, 11):
    print(numeros, end=' ', flush = True)
    sleep(0.5)
print('\n')

#contador de 10 a 0
for numeros2 in range(10, 0, -2):
    print(numeros2, end=' ', flush = True)
    sleep(0.5)
print("\n")

#coleta de dados para contagem personalizada
inicio = int(input('Digite um numero inicial:  '))
fim = int(input('Digite o numero final:        '))
salt = int(input('Pulando de quanto em quanto? '))

#se o usuario digitar a passada 0 o programa a trasforma em 1
if salt == 0:
    salt = 1

 #configuração pra contagens negativas
if fim < inicio:
    salt = -abs(salt) #- abs transforma o numero positivo em negativo
    inicio = inicio - 1
    fim = fim - 1

# define os valores para a contagem personalizada
contador(inicio, fim, salt)
