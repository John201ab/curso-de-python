boletim = list()
pessoa = dict()
pessoa['nome'] = input('digite o seu nome: ')
pessoa['media'] = float(input('digite sua média'))
boletim.append(pessoa.copy())
if boletim[0]['media'] >= 5:
    sit  = 'aprovado'
else:
    sit = 'reprovado'

for b in boletim:
    print(f'o nome é: {b["nome"]}')
    print(f'sua média é: {b["media"]}')
    print(f'você foi: {sit}')
