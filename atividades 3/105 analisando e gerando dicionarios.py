def calculadora(*valores, sit = False):
    """Função que analisa notas e situações de alunos
    resposta:contem as  notas do aluno
    sit: parametro opcional, indicando se deve ou não adicionar a situação
    return: dicionario com as informaçoes dam turma"""
    
    maior = 0
    for k, i in enumerate(valores):
        if i > maior:
            maior = i
    menor = maior
    for k, i in enumerate(valores):
        if menor > i:
            menor = i

    media = round(sum(valores) / total, 2)

    if media > 7:
        situação = 'boa '

    elif media < 7 and media > 5:
        situação = 'regular'

    else:
        situação =  'ruim'
    
    boletim = {'total' : total, 'maior' :  maior, 'menor' : menor, 'media' : media}

    if sit == True:
            boletim['situação'] = situação

    return(boletim)

sit=True

notas = (1, 3, 5, 8, 8,)


resposta = notas

resposta = calculadora(resposta)

print(resposta)