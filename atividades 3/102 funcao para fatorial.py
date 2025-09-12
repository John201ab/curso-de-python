def fatorial(valor):
    menos = valor 
    fatorado = 0
    for c in range(valor, 1, -1):      
        fatorado += menos * (c - 1)
        menos -= 1
    return(fatorado)

numero = int(input('Digite um numero a ser fatorado: '))

fatorado = fatorial(numero)
print(fatorado)