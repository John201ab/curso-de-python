from random import randint

pares = list()
aleatorio = list()
par = list()
 #função que sorteia 5 numeros entre 0 e 99
def sorteia():
    global aleatorio
    for k in range(0,5):
        aleatorio.append(randint(0, 100))

#função que faz a separação e soma de numeros pares
def somapar():
    global pares
    for v, l in enumerate(aleatorio):
        if l % 2 == 0:
            pares.append(l)

sorteia()
somapar()
print(f"os numeros são {aleatorio}")
par.append(sum(pares))
print(f'a soma de {pares} é {par}')