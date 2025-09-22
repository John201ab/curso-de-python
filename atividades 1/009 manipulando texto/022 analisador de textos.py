nome = str(input('digite seu nome completo: ')).strip()

m = nome.upper()
min = nome.lower()
num = len(nome.replace(' ',''))
prim = nome.split()

print(f"""seu nome em maiusculo é {m}
      em minusculo é: {min}
      sem espaçoes tem o total de: {num} caracteres
      e o primeiro nome tem {len(prim[0])} letras""")