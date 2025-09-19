def ficha (jogador = '<desconhecido>', gols = 0):
    """Função que com os dados fornecidos pelo usuário, exibe o nome e quantidade de gols de um jogador durante um campeonato"""
    return(f'o jogador {jogador} marcou {gols} gols no campeonato.')


nome = input('digite o nome do jogador: ')
gol  = input('gigite o numero de gols marcado por ele: ')

dados = ficha(nome, gol)
print(dados)