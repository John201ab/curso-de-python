estatisticas = list()
jogador = dict()
escolha = ""
jogos1 = list()
check = volta = 0

while escolha != 'N':
    jogador["nome"] = input('digite o nome do jogador: ')
    partidas = int(input('quantas partidas ele jogou? '))
    jogador["gols"] = list()
    
    for c in range(partidas):
        jogos = int(input(f'quantos gols ele marcou na {c+1}° partida? '))
        jogos1.append(jogos)
        
    jogador["gols"] = jogos1.copy()   
    escolha = input('deseja continuar? [S/N]').strip().upper()
    jogos1.clear()

    jogador["gols_totais"] = sum(jogador["gols"].copy())
    estatisticas.append(jogador.copy())

    if escolha == 'N':
        break
    
    if escolha not in ['S','N']:
        while escolha not in ['S','N']:
            escolha = input('Não entendi, digite novamente [S/N]').strip().upper()

    volta += 1


print(f'Nº {'Nome: ':>10} {'Gols: ':^20} {'Gols totais: ':>20}')
for loop, valor in enumerate(estatisticas):
    print(f'{loop} {valor["nome"]:>10} {str(valor["gols"]):^15} {valor["gols_totais"]:>20}')

while True:
    check = int(input('Deseja ver estatisticas de qual jogador? (999 para) '))

    if check == 999:
        break

    if check > volta:
        while check > volta:
            check = input('Digite um numero válido: ')  
            if check == 999:
                break

    if check <= volta:
        print(estatisticas[check])
        print(f'==DADOS DO JOGADOR {estatisticas[int(check)]["nome"].upper()}== ')
        for voltas,gols in enumerate(estatisticas[check]['gols']):
            print(f'no {voltas + 1}º fez {gols} gols')
            
print('Obrigado pela pesquisa e preferencia!')
    