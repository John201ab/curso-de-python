cor = ('\033[m,'            #0 - sem cor
        '\033[0;30;41m',    #1 - vermelho
        '\033[0;30;42m',    #2 - verde
        '\033[0;30;43m',    #3 - amarelo 
        '\033[0;30;44m',    #4 - azul
        '\033[0;30;45m',    #5 - roxo
        '\033[7;30m',       #6 - beanco
        )
def legenda(func):

    print(cor[1], end=' ')  # Começa cor verde
    help(func)
    print(cor[0], end=' ')      # Reseta cor


def linha (word):

    print(cor[3], end=' ')
    print('~' * (len(word) + 2))
    print(word)
    print('~' * (len(word) + 2))
    print(cor[0], end=' ')

while True:

    linha("SISTEMA DE AJUDA")


    func = input('Função ou Biblioteca: ').strip().lower()

    if func == 'fim':
        linha('Até logo')
        break

    linha(f'ACESSANDO MANUAL DO COMANDO "{func}"')
    

    print(legenda(func))


#sim, está horrivel, mas essa personalização eu só copiei o guanabara

