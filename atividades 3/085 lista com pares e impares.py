numeros = [[],[]]

for contador in range(7): #faz o loop 7 vezes 
    valor = int(input(f'digite o {contador + 1}° valor: ')) #cada loop vai ser pedido pro usuario digitar um numeri
    if valor % 2 == 0: #se o resto da divisão for igual a 0, vai ser inserido na lista 0
        numeros[0].append(valor)
    else: #se nao, vai ser inserido na lista 1(juro q nao foi proposital kkkkkk)
        numeros[1].append(valor)
    valor = [] # a lista reseta pra receber novos valores 
numeros[0].sort() #ordena a lista após a adiçao de todos os numeros
numeros[1].sort()
print(f'ok, os valores impares digitados são: {numeros[1]} e os pares são {numeros[0]}')