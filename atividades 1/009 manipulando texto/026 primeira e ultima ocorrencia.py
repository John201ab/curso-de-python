frase = input('digite uma frase: ')
f = frase.lower()
a = f.count('a')
p = f.find('a')
u = f.rfind('a')

print(f"""nessa frase, a letra "a" aparece:
      {a+1} vezes, sendo a primeira vez na posição {p+1}
      e a ultima na posiçao {u+1}""")