valor = int(input('digite um valor: '))
chave = str(input('deseja continuar? [S/N]: ' )).upper().strip()
soma = media = maior = 0
contador = 1
menor = valor
while chave == 'S':
    valor = int(input('digite um outro valor: '))
    contador += 1
    soma += valor
    media = soma / contador
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    chave = str(input('quer continuar? [S/N]: ')).upper().strip()[0]
print(f'a média de valores é: {media}, o maior valor foi: {maior} e o menor: {menor}')