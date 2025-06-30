#listas usadas
boletim = []
aluno = []
notas1 = []
notas2 = []
nota = []
check = 0
while True: #enquanto for verdadeiro
    aluno.append(input('Digite o nome do aluno: '))
    notas1 = input('Digite a primeira nota: ')
    notas2 = input('digite a segunda nota: ')
    escolha = input('deseja parar? [S/N]: ').upper()

    nota.append(notas1[:]) #a lista nota recebe notas1
    nota.append(notas2[:]) #nota recebe notas2
    aluno.append(nota) #aluno recebe nota
    boletim.append(aluno[:]) #boletim recebe aluno, contem nome e as duas notas
    #todas essas listas ficam vazias dnv
    nota = []
    notas1 = []
    notas2 = []
    aluno = []

    if escolha == 'S': #se escolha for 's'
        break #tudo para
    
    else: #se nao
        while escolha not in ['S','N']: # enquanto escolhas nao for "s" ou "n"
            escolha = input('nao entendi, digite novamente: [S/N]').upper()

print('=-' * 30)
print(f'n°   {"NOME":<10}      {"NOTAS":>20}')
for c, alunos in enumerate(boletim): #vai passar item por item na lista, no caso nome e nota até acabar tudo
    print(f'{c} {alunos[0]:<20} {str(alunos[1]):>20}')
print('=-' * 30)

while check != '999': #verdadeiro enquanto for 999
    check = int(input(f'digite o numero do aluno para ve-lo ou 999 pra encerrar: '))
    print(f'{boletim[check]}') #procura o item na lista na posição q o usuario decidiu
