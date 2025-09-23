import moeda

p = float(input('Digite um valor: '))
print(f'a metade de {p} é {moeda.metade(p)}')
print(f'o dobro de {p} é {moeda.dobro(p)}')
print(f'aumentoando {p} em 10% temos {moeda.aumentado(p, 10)}')
print(f'reduzindo {p} em 13% temos {moeda.reduzido(p, 13)}')