city = input('em que cidade você nasceu? ').strip().lower()
c = city.split()
r = 'santo' in c[0]
print(f'ela começa com "santo"? {r}')