#tupla com todos os numeros
extenso = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez',
          'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
#input pra saber qual numero o usuario quer ler
numero = int(input('Digite um numero de 0 até 20: '))
#se o numero nao estiver entre 0 e 20
if 0 < numero > 20:
    int(input('Erro, escolha um numero de 0 a 20: '))
#se nao, mostra na tupla o numero na posiçao
else:
    print(extenso[numero])
