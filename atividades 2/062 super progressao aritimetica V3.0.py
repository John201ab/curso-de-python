print('''sabe como funciona a progressao aritimetica? vc escolhe um numero e um intervalo entre eles
e eu conto os primeiros 10 numeros dessa progressao''')
termo = int(input('digite o termo: ')) #a artir de qual numero vai começar a seuqnecia?
razao = int(input('digite a razao: ')) #pulando de quantos em quantos?
contador = 0 #vai receber quantos numeros a serao exibidos a seguir
acumulador = 0 #quantos numeros foram exibidos no total
escolha = 10 #mostrara os 10 primeiros termos depois quantos o usuario pedir

while escolha != 0: # enquanto escolha for diferente de 0:
    while contador < escolha: #laço de exibiçao
        print(termo , end = ' > ')
        termo += razao
        contador += 1
        acumulador += 1
        if contador == escolha: #petiçao pro usuario continuar ou sair
            escolha = int(input(' e ai? posso te mostrar mais quantos termos? \n[caso nao, digite 0 pra sair]: '))
            contador = 0
print(f'oh.. ok.  você viu durante esse programa {acumulador} termos, até mais ^^')