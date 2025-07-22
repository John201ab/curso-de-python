from random import randint
jogador = {}
placar = []
print('valores sorteados: ')
for c in range (1,5):
    jogador['pos'] = c
    jogador['num'] = randint(0,9)

    print(f'o jogador {c} tirou {jogador["num"]}')
    if c == 1:
        placar.append(jogador.copy())
    else:
        for p in placar:
            if jogador['num'] <= placar[p]['num']:
                placar.append(jogador.copy())
            else:
                placar.insert[-1](jpgador.copy())
for p in placar:
    print(p.items())