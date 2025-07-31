jogador = dict()

jogador["nome"] = input('digite o nome do jogador: ')
partidas = int(input('quantas partidas ele jogou? '))
jogador["gols"] = list()
jogador["gols_totais"] = 0
for c in range(partidas):
    jogos = int(input(f'quantos gols ele marcou na {c+1}° partida? '))
    jogador["gols"].append(jogos)

jogador["gols_totais"] = sum(jogador["gols"])
print('=-' * 50)
print(jogador)
print('=-' * 50)
for v,p in enumerate(jogador):
    print(f'O campo {p} tem valor {jogador[p]}')
print('=-' * 50)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for v,c in enumerate(jogador["gols"]):
    print(f'na {v + 1}° partida ele marcou {jogador["gols"][v]} gols')
print(f'foi um total de {jogador["gols_totais"]} gols')