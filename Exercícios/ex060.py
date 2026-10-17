n = int(input('Digite um número para saber o seu fatorial: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}\nO fatorial de {} é {}.'.format(f, n, f))
