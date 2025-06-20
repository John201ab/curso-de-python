boletim = []
aluno = []
notas = []
while True:
    aluno=(str(input('Digite o nome do aluno: ')))
    notas1=(int(input('Digite a primeira nota: ')))
    notas2=(int(input('digite a segunda nota: ')))
    escolha = input('deseja parar? [S/N]: ').upper()

    boletim.append([aluno],[notas1,notas2])
  

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