matriz = [[],[],[]]
pares = tercolu = seglin = 0
for loop in range (3): #esse loop vai contar uma volta quando o debaixo encerraras dele
    for cont in range (3): #esse vai exibir o input tres vezes, e reiniciar o contador quando o de cima girar
            
            valores = int(input(f'digite um valor para a posição: [{loop}:{cont}]'))
            matriz[loop].append(valores) #adiciona o valor em determinada posição
            
            if valores % 2 == 0: #se o resto da divizão for 2
                  pares += valores #pares vai receber esse numero

            if cont == 2: #se o for estiver em 2
                tercolu += valores #tercolu recebe esse valor, pq SEMPRE q o loop cont estiver em 2, o valor vai ser adicionado na segunda coluna


            valores = [] #limpa  a lista valores

print('=-' * 30)
print(f''' a matriz ficou:
      [{matriz[0][0]}|{matriz[0][1]}|{matriz[0][2]}]
      [{matriz[1][0]}|{matriz[1][1]}|{matriz[1][2]}] 
      [{matriz[2][0]}|{matriz[2][1]}|{matriz[2][2]}]
       ''') #exibe na tela os numeros de determinada posição
print('=-' * 30)

matriz[1].sort() #isola a segunda linha da matrix depois de exibir e ordena do menor ao maior
seglin = matriz[1][2] #pega o maior item da segunda linha

print(f''' a soma dos valores pares é: {pares}
 a soma doa valores da terceira coluna é: {tercolu}
 o maior da segunda linha é: {seglin}''')
