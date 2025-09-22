from datetime import date #tambem pós aula, nao conhecia até agr

ano = int(input('digite um ano qualqer e eu direi se ele é bisexto, ou 0 pra ver o ano atual: '))
if ano == 0:
    ano = date.today().year #esse 'if' foi pós exercicio, se ilude n

if ano % 4 == 0 and ano %100 !=0 or ano % 400 == 0:#pse, esse precisei olhar a resposta pra isso tb,
    # o bagui foi punk
    print(f'o ano {ano} é um ano bisexto')

else:
    print(f'o ano {ano} nao é um ano bisexto')