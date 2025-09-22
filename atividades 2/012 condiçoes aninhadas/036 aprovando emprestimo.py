valorcasa = float(input('olá fico feliz de querer orçar um emprestimo conosco!!\n '
                        'qual o valor da casa? R$'))

salario = float(input('otimo!! agora preciso do quanto o(a) senhor(a) ganha mensalmente: R$'))

tempo = float(input('em quantos anos planeja pagar?: '))

percentual = salario * (30/100)
parcela = ((valorcasa / (12 * tempo)))

if parcela > percentual:
    print(f"""sinto muito, a parcela será de {parcela:.2f}, o 
emprestimo não poderá ser realizado pois será inviavel pro senhor.""")
else:
    print(f"""BOAS NOTICIAS: seu emprestimo foi APROVADO!!!
    as parcelas serão no valor de {parcela:.2f}R$.""")