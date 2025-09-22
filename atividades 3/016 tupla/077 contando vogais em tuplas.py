palavras = ('aprender','programar', 'linguagem', 'python', 'curso','gratis','estudar','praticar'
            'trabalhar', 'mercado', 'programador', 'futuro')#tupla de palavras
vogais = 'aeiou' #vogais a se comparar
listinha = () #acumulador
for c in range(len(palavras)): #percorra toda tupla: palavras
    recorte = palavras[c] #pegue a palavra na posiçao c
    for letras in recorte: #soletre a palavra na posiçao: recorte
        if letras in vogais: #se existe a letra na tupla: vogais
            listinha += (letras,) #listinha recebe a letra e adicona ,
    print(f'na palavra: {recorte.upper()} temos: {listinha}')
    listinha = () #reseta a tupla
print('e é isso.')