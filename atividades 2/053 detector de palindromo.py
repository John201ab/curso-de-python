frase = str(input('diga-me uma frase, e eu direi se é um palindromo ou nao: ')).lower()
frases = frase.replace(' ','')

#frase ao contrario
pali = frases[::-1]

 #comparaçao das frases
if frases == pali:
    print(f'bom, realmente, {frase} é um palindromo, ao contrario fica {frases}')

else:
    print(f'calma ae amigão, parece q {frase} nao é um palindromo, ao contrario fica: {pali}')