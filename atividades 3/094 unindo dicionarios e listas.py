usuarios = list()
mulheres = list()
pessoas = dict()
loop = numulheres= acima = idades_totais = v = 0

while True:
    pessoas["nome"] = str(input('Digite seu nome: '))
    pessoas["sexo"] = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
    pessoas["idade"] = int(input('Digite sua idade: '))
    escolha = input('Deseja continuar? [S/N]').strip().upper()[0]

    usuarios.append(pessoas.copy())
    loop += 1
    idades_totais += pessoas["idade"]
    if pessoas["sexo"] == "F":
        mulheres.append(pessoas.copy())
        
    if escolha == 'N':
        break

media = idades_totais / loop

print(f'A) o grupo tem: {loop} pessoas')
print(f'B) a média de idade do grupo é: {media} anos')
print(f'C)as mulheres cadastradas foram: ')
for lopp, mulher in enumerate(mulheres):
    print(mulher["nome"], end=', ') 
    
print("\n D) lista das pessoas com idade acima da média: ")
for voltas, velhos in enumerate(usuarios):
    if velhos["idade"] >= media:
        print(f" {velhos} \n")
    