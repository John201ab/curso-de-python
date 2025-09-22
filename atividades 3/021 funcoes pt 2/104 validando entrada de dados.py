def leiaint(numero):
    validador = numero

    #valida se é numerico ou não
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
        numero = input(('ERRO! Digite um numero válido: ')).strip()
