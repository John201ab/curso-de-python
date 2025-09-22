expressao = input('digite uma expressão matematica e direi se é valida ou nao: ')
parenteseE = expressao.count('(')
parenteseD = expressao.count(')')
if parenteseE == parenteseD:
    print('sua expressão está correta :)')
else:
    print('sua expresão está errada :(')