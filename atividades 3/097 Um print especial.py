def mensagem(msg):
    tam = int(len(msg))
    print( '~' * (tam + 2))
    print(msg)
    print('~' * (tam + 2))

palavra = str(input('Digite uma frase: '))

mensagem(palavra)
