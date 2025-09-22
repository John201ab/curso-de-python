from datetime import datetime
pessoa = dict() #declarei o dicionario
data = datetime.now()
year = data.year #defini o ano com o ano  do sistema

pessoa["nome"] = str(input('digite seu nome: ')) #a resposta entrará como valor da chave "nome"
ano = int(input('digite seu ano de nascimento: '))
pessoa["idade"] = (year - ano)
pessoa["carteira"] = int(input('digite seu numero de carteira(0 não tem): ')) #a resposta entrará como valor
# da chave "nome"
if pessoa["carteira"] == 0: #se o valor da chave "carteira" for 0
    print('ctps tem o valor 0 ')
    print(pessoa)
    for v,p in enumerate(pessoa): #esse loop vai passar por todas as chaves do dicionario
        print(f'{p} tem o valor: {pessoa[p]}') # "P" é a chave e "pessoa[p]" é: dentro da lista pessoa,
        # item da chave "p". "P" vai mudar a chave a cada loop e quando chegar no final o programa para.
else:
    pessoa["contratacao"] = int(input('digite o ano de contratação: ')) #a resposta entrará como valor da
    # chave "contratacao"
    pessoa["salario"] = str(input('digite o seu salário: ')) #a resposta entrará como valor da chave "salario"
    pessoa["aposentadoria"] = (pessoa["contratacao"] + 35) - year #a resposta entrará como valor da chave "aposentadoria"

    print(pessoa)
    for v,p in enumerate(pessoa):  #esse loop vai passar por todas as chaves do dicionario
        print(f'{p} tem o valor: {pessoa[p]}') # "P" é a chave e "pessoa[p]" é: dentro da lista pessoa,
        # item da chave "p". "P" vai mudar a chave a cada loop e quando chegar no final o programa para.
