jogador = dict()
jogador["gols"] = list()  

jogador["nome"] = input('digite o nome do jogador: ') # crio a chave "nome" e peço pra preencher
partidas = int(input('quantas partidas ele jogou? ')) 
jogador["gols_totais"] = 0  # crio a chave "gols totais" e peço pra preencher
for c in range(partidas): #um loop com voltas definidas pelo numero de partidas jogadas
    jogos = int(input(f'quantos gols ele marcou na {c+1}° partida? '))
    jogador["gols"].append(jogos) # a cada loop um valor vai ser acrescentado na lista

jogador["gols_totais"] = sum(jogador["gols"]) # faz a soma de toda a lista gols 

print('=-' * 50)
for v,p in enumerate(jogador): #cria um loop definido pela quantidade de chaaves dentro do dicionário
    print(f'O campo {p} tem valor {jogador[p]}')
print('=-' * 50)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for v,c in enumerate(jogador["gols"]): #um loop definido pela quantidade de gols
    print(f'na {v + 1}° partida ele marcou {jogador["gols"][v]} gols')
print(f'foi um total de {jogador["gols_totais"]} gols')