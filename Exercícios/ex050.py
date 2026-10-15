num = 0
for soma in range(1, 7):
    n = int(input('Digite o {}° valor para somar: '.format(soma)))
    if n % 2 == 0:
        num += n
print('A soma dos números digitados é {}.'.format(num))