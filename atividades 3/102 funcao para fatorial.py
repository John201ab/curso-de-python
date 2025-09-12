def fatorial(valor, mostrar = False):
    fatorado = 1
    for c in range(valor, 0, -1):      
       fatorado *= c
    return(fatorado)

numero = int(input('Digite um numero a ser fatorado: '))

fatorado = fatorial(numero)
print(fatorado)