pessoa = dict()  #declaro "pessoa" como um dicionario
pessoa['nome'] = str(input('digite o seu nome: ')) # crio a chave "nome" e peço pra preencher
pessoa['media'] = float(input('digite sua média: ')) # crio a chave "média" e peço pra preencher
if pessoa['media'] >= 5:  # se o valor de "média" for maior que 5
    pessoa["situacao"]  = 'aprovado'  # crio a chave "situação" e preencho com "aprovado"
else:  #se não
    pessoa["situacao"]  = 'reprovado' ### crio a chave "situação" e preencho com "reprovado"

print('=+' * 30)
for key, value in pessoa.items():  ## faz voltas passando passando por cada item do dicionario
    print(f'{key} é igual a {value}')
   
