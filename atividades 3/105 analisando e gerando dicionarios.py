def calculadora(valores):
    
    total = len(notas)
    print(total)

    maior = 0
    for k, i in enumerate(valores):
        if i > maior:
            maior = i
    menor = maior
    for k, i in enumerate(valores):
        if menor > i:
            menor = i

    media = sum(valores) / total


    boletim = {'total' : total, 'maior' :  maior, 'menor' : menor, 'media' : media}

    return(boletim)


notas = (1, 3, 5, 7, 8, 8)


resposta = notas

calculadora(resposta)

print(resposta)