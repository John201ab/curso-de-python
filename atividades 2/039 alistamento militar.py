from datetime import datetime #colocar musica de exercito de fundo e return
anos = int(input("""\033[2;33mOLÁ MEU JOVEM, VAMOS DESCOBRIR SE VOCÊ ESTÁ APTO PARA SERVIR SEU PAÍS?
PODEMOS COMEÇAR COM: EM QUE ANO VOCÊ NASCEU?? \033[m"""))

hoje = datetime.now().year
idade = hoje - anos
passe = (idade - 18)
ideal = (anos + 18)
faltam = (18 - idade)

if idade < 18:
    print(f'\033[2;33mbom ainda é um pouco cedo para se alistar, você tem {idade} anos, faltam {faltam} anos\n'
          f'pro seu alistamento, volte em {ideal} \033m')

elif idade == 18:
    print('\033[2;33mPARABENS PELO COMPROMISSO, É O ANO IDEAL PRO ALISTAMENTO, \n'
          'ACREDITO QUE VAMOS NOS DAR BEM!!!\033[2;33m')

else:
    print(f'\033[2;33mJA PASSOU DA HORA DE SE ALISTAR SOLADADO, VOCÊ TEM {idade} ANOS,\n'
          f' DEVERIA TER SE ALISTADO EM {ideal}, HÁ {passe} ANOS ATRÁS !!!\033[2;33m')