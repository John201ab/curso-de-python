materiais = ('lapis',1.75,
             'borracha',2.00,
             'caderno',15.00,
             'estojo',25.00,
             'transferidor',4.20,
             'compasso',9.00,
             'mochila',120.32,
             'canetas',22.30,
             'livro',34.90) #toda tupla de materiais
for itens in range(0,len(materiais),2):#percorra toda  extensao da tupla pulando de 2 em 2
    print(f'{materiais[itens]:.<30}R$: {materiais[itens+1]:>7}') #itens na posiçao "itens" pra
    # deireita e pontos pra completar 30 caracteres; itens na posiçao itens+1 pra direita