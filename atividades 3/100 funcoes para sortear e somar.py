from random import randint


pares = list()
aleatorio = list()
par = list()

def sorteia():
    global aleatorio
    for k in range(0,5):
        aleatorio.append(randint(0, 100))

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