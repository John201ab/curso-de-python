pesos = []#lista de pesos
for c in range(5):#loop para inputs
 peso = float(input(f'digite o peso da {c} pessoa: '))
 pesos.append(peso)#adiciona os inputs da lista
maior = max(pesos)#escolhe o item de maior valor da lista
menor = min(pesos)#escolhe o item com menor valor da lista

print(f' o maior peso lido foi: {maior} , e o menor foi: {menor}')#printa o maior e menor