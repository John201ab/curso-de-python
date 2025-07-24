from random import randint
jogador = {}
placar = []
print('valores sorteados: ')
for c in range (1,5):
    jogador['pos'] = c
    jogador['num'] = randint(0,9)
    placar.append(jogador.copy())
    print(f'o jogador {c} tirou {jogador["num"]}')
ordenado = sorted(placar, key=lambda p: p['num'], reverse=True)

print('=' * 50)
for p in ordenado:
    print(f'o jogador {p["pos"]} jogador tirou {p["num"]} pontos')

print('=' * 50)
