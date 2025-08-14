usuarios = list()
mulheres = list()
pessoas = dict()
loop = numulheres= acima = idades_totais = v = 0

while True:
    pessoas["nome"] = str(input('Digite seu nome: '))
    pessoas["sexo"] = str(input('Digite seu sexo [H/M]: ')).strip().upper()[0]
    pessoas["idade"] = int(input('Digite sua idade: '))
    escolha = input('Deseja continuar? [S/N]').strip().upper()[0]

    usuarios.append(pessoas.copy())
    loop += 1
    idades_totais += pessoas["idade"]
    if pessoas["sexo"] == "M":
        numulheres += 1
        mulheres.append(pessoas.copy())
        
    if escolha == 'N':
        break
 

media = idades_totais / loop


print(f'o grupo tem: {loop} pessoas')
print(f' a média de idade do grupo é: {media} anos')
print(f'as mulheres cadastradas foram: ')
for lopp, mulher in enumerate(mulheres):
    print(mulher["nome"])
print("lista das pessoas com idade acima da média: ")
for voltas, velhos in enumerate(usuarios):
    if velhos["idade"] >= media:
        print(f"nome:{velhos["nome"]}")
    