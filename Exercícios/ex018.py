import math
an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
print('O seno de {} é {:.2f}.'.format(an,seno))
cos = math.cos(math.radians(an))
print('O cosseno de {} é {:.2f}.'.format(an,cos))
tan = math.tan(math.radians(an))
print('A tangente de {} é {:.2f}.'.format(an,tan))
