velocidade  = int(input('qual a velocidade do seu veiculo? '))
valormulta = velocidade - 80
multa = valormulta * 7.00
if velocidade >= 81:
    print(f"""você foi multado por que: sabendo que o limite é 80 você passou a {velocidade}, sabendo disso, 
o valor da multa é de {multa}""" )
else:
    print('bom, tudo parece certo por aqui')
