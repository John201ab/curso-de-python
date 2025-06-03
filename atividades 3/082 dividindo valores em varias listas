from time import sleep
validador = 'S'
todos = []
valores = int(input('beleza, digite um valor e vou dizer com precisão se ímpar ou par: ')) #esse input está fora do loop pra plmns a primeira mensagem ser diferente
todos += [valores] #valor do input adicionado na lista

while validador == 'S': #enquanto o validador for 'S':
    valores = int(input('digite outro valor:')) #usuario digita um novo valor 
    todos += [valores] #lista todos recebe o valor do usuario
    validador = input('deseja continuar? [S/N]').upper() #validador vai ser alterado pelo usuario fazendo o loop continuar ou nao de acordo com a vontade dele
    if validador not in ['S', 'N']: #se o usuario digitar algo q nao seja 's' ou 'n':
        while validador not in ['S','N']: #vai entrar em um loop até digitar certo
            validador = input('opção nao identificada, digite "S" ou "N" ').upper()
par = []
impar = []
for item in range(len(todos)): # vai varrer a lista de ponta a ponta:
    if  todos[item] % 2 == 0: #se o resto da divisão do item por 2 for igual a '0'
        par.append(todos[item]) #o item vai pra lista par
    else: #caso o contrario vai pra lista impar
        impar.append(todos[item])
   
print('bom, com os valores que temos até então...')
sleep (1)
print('pera, deixa eu ver..')
sleep(2)
print('esse é impar...')
sleep(2)
print('esse também...')
sleep(2)
print(f'CERTO. a primeira lista com todos os valores é: {todos}\n' 
      f'temos os valores pares: {par} \n'
      f'e tambem temos os impares: {impar}')
print('e é isso ai, até a proxima!')

