usuarios = list()
pessoas = dict()
loop = mulheres = acima = idades_totais = 0

while True:
    pessoas["nome"] = str(input('Digite seu nome: '))
    pessoas["sexo"] = str(input('Digite seu sexo [H/M]: ')).strip().upper()[0]
    pessoas["idade"] = int(input('Digite sua idade: '))
    escolha = input('Deseja continuar? [S/N]').strip().upper()[0]

    usuarios.append(pessoas.copy())
    loop += 1
    idades_totais += pessoas["idade"]
    if pessoas["sexo"] == "M":
        mulheres += 1
    if escolha == 'N':
        break
 

media = idades_totais / loop

for k, c in enumerate(usuarios):
    print(usuarios["nome"])