from random import randint
jogador = {}
placar = []
print('valores sorteados: ')
for c in range (1,5): ##faz o loop rodar 5 vezes
    jogador['pos'] = c  ##pega a poisção do loop q vai ser a identificação do jogador
    jogador['num'] = randint(0,9) ##sorteia um numero aleatório de 1 até 9
    placar.append(jogador.copy())  #a lista placar recebe o dicionario jogador
    print(f'o jogador {c} tirou {jogador["num"]}')
ordenado = sorted(placar, key=lambda p: p['num'], reverse=True) #assim q o loop acabar, essa linha o ordena de forma decrescente

print('=' * 50)
for p in ordenado: ##vai rodar o numero de dicioários dentro da lista
    print(f'o jogador {p["pos"]} jogador tirou {p["num"]} pontos')  ##exibe as caracteristicas dos jogadores

print('=' * 50)
