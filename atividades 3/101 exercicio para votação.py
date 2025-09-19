from datetime import date

def voto(idade):
    calendario = date.today()
    ano = calendario.year
    votar = ano - idade

    if votar < 18:
        return(f'Você tem {votar} anos. \n Situação: negado')
    
    elif votar > 18 and votar < 60:
        return(f'Você tem {votar} anos. \n Situação: Obrigatório')
    
    else:
        return(f'Você tem {votar} anos. \n Situação: Opcional')


idade = int(input('digite seu ano de nascimento: '))
situação = voto(idade)
print(situação)