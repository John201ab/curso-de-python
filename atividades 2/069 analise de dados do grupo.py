print('-' * 20)
print('cadastre-se!')
print('-' * 20)
sexo = ''#declaraçoes da variaveis
escolha = ''
de_maiores = 0
homens = 0
mocas_sub_20 = 0
while escolha in 'Ss':#enquanto o usuario quiser continuar (escolha for s)
    idade = int(input('digite sua idade:'))
    sexo = str(input('você é homem ou mulher?[H/M]')).strip()[0]
    while sexo not in 'HhMm': #enquanto sexo nao for h ou m
        sexo = str(input('você é homem ou mulher?[H/M]')).strip()[0]
    if idade >= 18: #se idade for maior que 18, de maior recebe +1
        de_maiores += 1
    if sexo in 'Hh':#se o usuario cadastrado for homem, homem recebe +1
        homens += 1
    if idade < 20 and sexo in 'Mm': #se for mulher e menor de 20, moças_sub_20 recebem +1
        mocas_sub_20 += 1
    print('...' * 20)
    escolha = str(input('quer cadastrar mais alguem? [s/n]')).strip()[0] #quebra do loop se deseja continuar
    print('...' * 20)

print('=====RESULTADOS=====')
print(f'''temos entao, {de_maiores} pessoas de maior
temos {homens} de homens cadastrados 
e {mocas_sub_20} mulheres com menos de 20 anos''')