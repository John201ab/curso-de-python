valores = []
maior = menor = cont = ()
for cont in range(0,5): #repita por 5 vezes
    valores.append(int(input('digite um numero: '))) #input que sera repetido pro usuario

for cont in range(len(valores)): #loop que vai girar de acordo com o tamanho da lista
    if valores[cont] == max(valores): #se o valor for igual o maior da lista...
        maior += cont, #maior vai receber o valor da posiçao do item
    elif valores[cont] == min(valores): #agora se o valor for igual ao menor...
        menor += cont, #menor vai receber o valor do item na lista
print('=-' * 20)
print(f''' a lista completa é: {valores}
      o maior valor digitado foi: {max(valores)} na posição: {maior} 
      e o menor foi: {min(valores)} na posiçao: {menor}''')