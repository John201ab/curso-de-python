from random import randint

par = list()
aleatorio = list()
pares = list()
 #função que sorteia 5 numeros entre 0 e 99
def sorteia():
    global aleatorio
    for k in range(0,5):
        aleatorio.append(randint(0, 100))

#função que faz a separação e soma de numeros pares
def somapar():
    global par
    for v, l in enumerate(aleatorio):
        if l % 2 == 0:
            par.append(l)

sorteia()
somapar()
print(f"os numeros são {aleatorio}")
pares.append(sum(par))
print(f'a soma de {par} é {pares}')