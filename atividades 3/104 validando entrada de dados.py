def leiaint(numero):
    validador = numero
    if validador.isnumeric():
        return(f'Você digitou o número: {numero}')
    else:
        return None
 
        
numero = input('Digite um número: ').strip()

while True:
    resultado = leiaint(numero)

    if resultado:
        print(resultado)
        break
    else:
        numero = input(('Digite um numero válido: ')).strip()
