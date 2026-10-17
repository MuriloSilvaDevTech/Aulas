n1 = 0
n2 = 1
c = 2
print('—' * 40)
print('{: ^40}'.format('Sequência de Fibonacci'))
print('—' * 40)
ter = int(input('Quantos termos você quer mostrar? '))
print('~' * 40)
print('{} → {}'.format(n1, n2), end=' → ')
while c < ter:
    n3 = n2 + n1
    print('{}'.format(n3), end=' → ')
    n1 = n2
    n2 = n3
    c += 1
print('FIM')
print('~' * 40)