from random import randint
from time import sleep

cartela = []
jogo = []
contador = 0
jogos = int(input('quantos jogos vao ser sorteados?')) #pergunta ao usuario o numero de cartelas que elo usuario quer

for loop in range(jogos): #vai fazer o proximo loop se repetir o numero de vezes que o usuario quer
    while contador < 6: #enquanto o numero de itens na cartela for menor que 6
        sorte = randint(0,99) #sorteia numeros aleatorios entre 0 e 99
        if sorte not in jogo: #se sorte (numero sorteado) nao estiver na 'cartela' atual
            jogo.append(sorte) #o programa adiciona
            contador += 1 #e o contador soma +1
                 #ao sair do loop while
    contador = 0 #o contador zera
    cartela.append(jogo) #cartela adiciona a sublista 'jogo'
    jogo = [] #jogo fica limpo pra receber novos numeros

print(f"{f'sorteando {jogos} jogos':=^50}")  #titulo centralizado
for c in range(len(cartela)): #esse loop vai girar o numero de vezes q o usuario escolheu no começo
    print(f'jogo {c + 1}: {str(cartela[c]):>25}') #exibe tudo com uma formataçao em teste
    sleep(1)   #aguarda 1 segundo entre uma exibiçao e outra
print(f"{'BOA SORTE':=^50}")