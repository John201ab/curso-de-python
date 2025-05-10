num = int(input('digite qualquer numero de 0 a : 9999: '))

u = num // 1 % 10
c = num // 10 %10
d = num // 100 %10
m = num // 100 % 10

print(f"""a unidade é: {u}
a dezena é: {c}
a centena é: {d}
o milhar é: {m}""")
