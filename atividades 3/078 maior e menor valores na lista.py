valores = []
maior = menor = cont = ()
for cont in range(0,5): #repita por 5 vezes
    valores.append(int(input('digite um numero: '))) #input que sera repetido pro usuario
if valores == max(valores): #se o valor for o maximo da lista
    maior = cont #maior recebe esse valor
if valores == min(valores): #se o valor for o menor da lista
    menor = cont #menor recebe valor
print(f'o maior valor digitado foi: {max(valores)} na posição {maior} :e o menor foi: {min(valores)} na posiçao: {menor}')