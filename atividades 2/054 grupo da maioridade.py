from datetime import datetime
#contador
maior = 0
menor = 0
ano = datetime.now().year

print('Olá, tudo bem? Desculpa a pergunta, mas: ')
#loop
for c in range (7):
    nascimento = int(input(f'Qual o ano de nascimento da {c}º  pessoa?'))
    #calculara as idades
    idade = ano - nascimento

    #separador de idades
    if idade >= 21:
        maior += 1

    else  :
        menor += 1

print(f'Bom,ao final de tudo descobrimos que {maior} pessoas sao maiores de idade e {menor} menores.')
