print('''======john's store========''')

valor = float(input('digite o valor da sua compra: R$'))

print('qual a forma de pagamento?\n'
      '[1] á vista dinheiro\n'
      '[2] á vista cartão  \n'
      '[3] 2x no cartão\n'
      '[4] 3x ou mais no cartão')
escolha = input('qual a opção?')
desconto = valor - (valor * 10 / 100)
desconto2 = valor - (valor * 5 / 100)
parcela =  valor / 2
juros = valor * 20 / 100
if escolha == '1' :
    print(f'''com o pagamento sendo a vista, você recebe um desconto de 10%, fazendo
    o valor sair de: {valor} para: {desconto}''')

elif escolha == '2' :
    print(f'''com o pagamento sendo á vista no cartao , você recebe um desconto de 5%, fazendo
    o valor sair de: {valor}, para {desconto2}''')

elif escolha == '3' :
    print(f'''o pagamento será feito em 2x de: {parcela}, sem juros''')

else:
    escolha == '4'
    parc = int(input('em quantas vezes será parcelado?'))
    parcela2 = (valor + (valor * 20 / 100)) / parc
    total = valor +  juros

    print(f'''o pagamento será feito em {parc} vezes, o valor das parcelas será de: {parcela2:.2f}R$ com 
    {juros:.2f}R$ de juros, fazendo a compra sair de: {valor}R$ e custar: {total}R$ ''')

print('tenha um bom dia ^^')