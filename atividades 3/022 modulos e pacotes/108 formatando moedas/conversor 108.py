import moeda

p = float(input('Digite um valor: '))
print(f'a metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'o dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'aumentoando {moeda.moeda(p)} em 10% temos {moeda.moeda(moeda.aumentado(p, 10))}')
print(f'reduzindo {moeda.moeda(p)} em 13% temos {moeda.moeda(moeda.reduzido(p, 13))}')