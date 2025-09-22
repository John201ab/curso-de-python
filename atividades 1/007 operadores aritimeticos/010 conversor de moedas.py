rs = float(input('Digite o valor que você tem na carteira: R$ '))
us = 4.94
eu = 5.39
conv_dolar = rs / us
conv_euro = rs / eu
print('Com R$ {:.2f} você pode comprar US$ {:.2f} ou € {:.2f}'.format(rs, conv_dolar, conv_euro))

