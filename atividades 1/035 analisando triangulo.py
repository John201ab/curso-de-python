print ('=-' * 15)
print ('analisador de triangulo')
print ('=-' * 15)

base = float(input('primeiro segmento: '))
base1 = float(input('segundo segmento: '))
base2 = float(input('terceiro segmento: '))

if base + base1 > base2 and base2 + base1 > base and base + base2 > base:

    print (' com essas medidas é possivel fazer um triangulo')

else:

    print ('infelizmente, não é possivel fazzer um triangulo')
