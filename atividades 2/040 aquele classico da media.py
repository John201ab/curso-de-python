nota1 = float(input('Olá, vamos descobrir se você passou de  ano? digite a nota do primeiro bimestre'))
nota2 = float(input('digite agora a nota do segundo bimestre'))

final = (nota1 + nota2) / 2

if final > 6.9:
    print(f'PARABENS!! sua media final foi: {final}, você foi aprovado.')

elif final > 5 and final < 6.9:
    print(f'sua nota final foi: {final}, ou seja, você ficou de recuperação, se esforçe mais!')

else:
    print(f'infelizmente, sua nota foi: {final}, você reprovou, mais sorte ano que vem.')