l=float(input('A largura da parede em metros é: '))
a=float(input('A altura da parede em metros é: '))
area = l * a
print('A área desta parede é {}m²'.format(area))
print('A quantidade de litros de tinta necessária para pintar essa parede é {:.1f}L.'.format(area/2))