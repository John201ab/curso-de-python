# função que dita se o voto é obrigatório ou não
def voto(idade):

    from datetime import date #dentro da função pra ser carregado apenas dentro dela

    calendario = date.today()#-|
    ano = calendario.year     #|- coleta de dados
    votar = ano - idade      #_|

    if votar < 18:
        return(f'Você tem {votar} anos. \n Situação: negado')
    
    elif votar > 18 and votar < 60:
        return(f'Você tem {votar} anos. \n Situação: Obrigatório')
    
    else:
        return(f'Você tem {votar} anos. \n Situação: Opcional')



idade = int(input('digite seu ano de nascimento: ')) #solicita o ano de nascimento
situação = voto(idade) #chama a função e manda a slocitação 
print(situação)