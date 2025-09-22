n = 0
contador = 0
print('digite um numero, se for par vou somar, se nao, vou desconsiderar')
for c in range (0,6):
    num = int(input('digite aqui: '))
    if num % 2 == 0:
        n+=num
        contador += 1
print(f'a soma de todos os {contador} pares deu: {n} ')

