n = int(input('Digite um número para ver sua tabuada: '))
print('{:=^40}'.format(' TABUADA DO {} '.format(n)))
for c in range(0, 11):
    print('{} X {:2} = {}'.format(n, c, n * c))
print('=' * 40)