chance = ()
while chance not in ['S', 'N']:  # enquanto escolhas nao for "s" ou "n"
    chance = input('nao entendi, digite novamente: [S/N]').upper().strip()

    if chance == 'S' or 'N':  # se escolha for 'sim' o loop para
        chance = ()
        escolha = ()
        break

    else:  # se não, as variaveis chance e escolha sao limpas pra receber novos valores
        chance = ()
        escolha = ()