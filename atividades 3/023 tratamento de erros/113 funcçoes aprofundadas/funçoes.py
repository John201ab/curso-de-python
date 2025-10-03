def leiaint():
    while True:

        dado = input('digite um numero inteiro:')
        try:
            int(dado)
        
        except ValueError: 
            if dado =='':
                dado = 0
                print('\033[32mO Usuário não quis digitar um valor\033[m')
                return dado 
            else:
                print('\033[31mErro! esse numero não é um inteiro\033[m')
        else:
            return(dado)



def leiafloat():
    while True:
        dado = (input('digite um numero: '))

        try:
            int(dado)
            
        except ValueError:
            if dado == '':
                dado = 0
                print('\033[32mO usuário não quis digitar nada\033[m')
                return dado
            
            else:
                print('\033[31mO valor não é um inteiro\033[m')

        else:
            return(dado)

