def fatorial(valor, mostrar = 'n'):

    from time import sleep
    
    fatorado = 1

    if mostrar == 's':
        for c in range(valor, 0, -1):      
            fatorado *= c
            sleep(0.1)
            print(c, end=' * ' )
        return(fatorado)
    
    else:
        for c in range(valor, 0, -1):      
            fatorado *= c
        return(fatorado)
    """Função dedicada a resolver problemas de fatorial, sendo "numero" o numero q o usuario escoler pra fatorar e validação caso o usuario queira ver a operação completa ou noção"""
   

numero = int(input('Digite um numero a ser fatorado: '))
#solicitação pra exibir ou não o preocesso de fatoração

validacao = input('deseja ver o processo de fatoração? [S/N] ').lower().strip()
#caso o usuário digite 0, o valor vai ser mudado pra 1 automaticamente

if numero <= 0:
    numero = 1
fatorado = fatorial(numero,validacao)
print(fatorado)