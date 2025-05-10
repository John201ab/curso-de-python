from datetime import datetime
idade = int(input('qual a sua categoria, vamos descobrir? digite o ano do seu nascimento:'))

ano = datetime.now().year

hoje = ano - idade

if hoje < 10:
    print(f'você tem {hoje} anos. até os  anos, sua categoria é: mirim')

elif hoje > 9 and hoje < 15:
    print(f' você tem {hoje} anos. até os 14 sua categoria é: infantil')

elif hoje > 14 and hoje < 20:
    print (f' você tem {hoje} anos. até os 19 sua categoria é: junior ')

elif hoje == 21:
    print(f' voce tem {hoje}, a categoria dos "21" é: sênior')

else:
    print(f'você tem mais de 21, sua categoria é: master{hoje}')
