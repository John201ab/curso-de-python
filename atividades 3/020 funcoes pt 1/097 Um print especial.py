def mensagem(msg):
    tam = int(len(msg))
    print( '~' * (tam + 2))
    print(f' {msg}')
    print('~' * (tam + 2))

palavra = str(input('Digite uma frase: '))

mensagem(palavra)
