boletim = []
aluno = []
notas = []

while True:
    aluno.append(input('Digite o nome do aluno: '))
    notas.append(input('Digite a primeira nota: '))
    notas.append(input('digite a segunda nota: '))
    escolha = input('deseja parar? [S/N]: ').upper()

    aluno.append(notas[:])
    boletim.append(aluno[:])
  

    if escolha == 'S':
        break
    
    else:
        while escolha not in ['S','N']:
            escolha = input('nao entendi, digite novamente: [S/N]').upper()

print('=-' * 30)
print(f'n°   {"NOME":<10}      {"NOTAS":>20}')
for c, alunos in enumerate(boletim):
 print(f'{c} {alunos[c]:<20} {alunos[0][0]:>20}')
 print('=-' * 30)