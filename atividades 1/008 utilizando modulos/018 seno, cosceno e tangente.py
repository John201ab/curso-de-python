from math import cos, sin,tan, radians
angulo = int(input('digite um angulo:'))
print(f'se o angulo é {angulo}, o seno é {sin(radians(angulo)):.2f}, o cosceno é: {cos(radians(angulo)):.2f}'
      f' e a tangente é: {tan(radians(angulo)):.2f}')