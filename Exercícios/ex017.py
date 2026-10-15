co = float(input('O comprimento do cateto oposto é '))
ca = float(input('O comprimento do cateto adjacente é '))
hi = (co ** 2 + ca ** 2) ** 0.5
print('O comprimento da hipotenusa é {:.2f}.'.format(hi))

'''from math import hypot
ca = float(input('O comprimento do cateto adjacente é '))
co = float(input('O comprimento do cateto oposto é '))
print('A hipotenusa é {:.2f}.'.format(hypot(ca,co)))'''