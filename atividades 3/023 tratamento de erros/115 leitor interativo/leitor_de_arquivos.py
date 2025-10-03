import sys
import os

# MENU DE SELEÇÃO
def selecao():
    titulo('MENU PRINCIPAL')
    escolha = input('''
1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa
3 - Sair do sistema
                    
Escolha uma opção acima: ''')
    while True:
        if escolha.strip() == '1':
            visualizar()
            break
        elif escolha.strip() == '2':
            dadosCadastrais()
            break
        elif escolha.strip() == '3':
            print('Encerrando...')
            sys.exit()
        else:
            while True:
                chance = input('Digite uma opção válida: ')

                if chance in ['1', '2', '3']:
                    escolha = chance
                    break

#SOLICITA NOME E IDADE
def dadosCadastrais():
    titulo('CADASTRO')
    nome = input('digite um nome: ')
    idade= input("digite uma idade: ")
    validador(nome, idade)


#EXIBE A LISTA COMPLETA PARA O USUÁRIO
def visualizar():
    titulo('PESSOAS CADASTRADAS')

    if not os.path.exists('arquivo.txt'):
        with open('arquivo.txt', 'w') as f:
            print('Arquivo criado! Nenhuma pessoa cadastrada ainda.')
    else:
        with open('arquivo.txt', 'r') as arquivo:
            conteudo = arquivo.read()
            if conteudo.strip() == "":
                print("Nenhuma pessoa cadastrada.")
            else:
                print(conteudo)

    continuar()

#VALIDA SE PODE CADASTRAR NOME E IDADE
def validador(nome, idade):

        try:
            idade = int(idade)
        except:
             idade = input('digite apenas numeros: ')

        while True:
            if nome.strip() == "" or nome.strip().isnumeric():
                nome = input("digite um nome válido: ")
            else:
                break


             
        with open('arquivo.txt', 'a') as arquivo:  
            arquivo.write(f'{nome} {idade:.>20} anos\n')
        print(f'Novo nome: {nome} adicionado com sucesso!')
        continuar()


#TITULO
def titulo(texto):
    print(f'--' * 20)
    print(f'{texto:^40}')
    print(f'--' * 20)

#VALIDADOR DE CONTINUIDADE
def continuar():
    escolha = input('deseja continuar? [S/N]').strip().lower()
    if escolha not in ['s', 'n']:
        while True:
            chance = input('Digite uma opção válida: ')
            if chance in ['s', 'n']:
                    escolha = chance
                    break
            
    elif escolha == 'n':
        print('encerrando...')
        sys.exit()
    
    else:
        print('Você escolheu continuar')
        