#listas usadas
boletim = []
check = 0
while True: #enquanto for verdadeiro
    aluno = input('Digite o nome do aluno: ')
    notas1 = float(input('Digite a primeira nota: '))
    notas2 = float(input('digite a segunda nota: '))
    escolha = input('deseja parar? [S/N]: ').upper()
    media = (notas1 + notas2) / 2
    boletim.append([aluno,[notas1,notas2],media])

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
    print(f'{c} {alunos[0]:<20} {str(alunos[2]):>20}')
print('=-' * 30)

while True: #verdadeiro enquanto for 999
    check = int(input(f'digite o numero do aluno para ve-lo ou 999 pra encerrar: '))
    if check == '999': #se o check for igual a '999'
        break # o programa para

    else:
        print(f'{boletim[check][0]}    {boletim[check][1]}') #procura o item na lista na posição q o usuario decidiu

