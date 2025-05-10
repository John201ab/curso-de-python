#contadores e acumuladores
homensmaisvelhos = ''
idademaior = 0
contador = 0
idades = 0
#loop de inputs
for c in range (4):
    nome = str(input('digite um nome: '))
    idade = int(input('digite sua idade: '))
    sexo = str(input('é homem ou mulher? [H/M]: ')).upper()
    idades = idade
    #conta e acumula nome e idade de homens mais velhos
    if sexo == 'H':
        if idade > idademaior:
            homensmaisvelhos = nome
            idademaior = idade
    #acumula quantas mulheres tem menos de 20
    if sexo == 'M':
        if idade < 20:
            contador += 1
#calcula a media das idades
mediaidade = idades / 4
#printa o resultado
print(f'''a média de idade no grupo é: {mediaidade}, o homem mais velho é: {homensmaisvelhos},
 com  {idademaior} anos. e temos {contador} mulheres de menor''')