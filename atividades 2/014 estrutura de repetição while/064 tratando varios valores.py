print('quer jogar um jogo? digite quantos numeros quiser q eu vou somar sem errar')
numero = int(input('digite um numero'))
soma = 0
contador = 0
while numero != 999:
    numero = int(input('digite o quanto aguentar ou 999 pra parar'))
    soma += numero
    contador += 1
print(f'foram digitados {contador} numeros, e a soma entre todos deu: {soma-999}')
print('fim')
