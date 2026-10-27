lista = []
pares = []
impares = []
pos = p = q = 0
while True:
    lista.append(int(input('Digite um número: ')))
    opcao = input('Quer continuar? [S/N] ').upper().strip()[0]
    if opcao in 'N':
        break
print('—' * 60)
print(f'A lista completa é {lista}')
print(f'A quantidade de elementos na lista é {len(lista)}.')
lista.sort()
print(f'A lista em ordem crescente é {lista}')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é {lista}')
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        p += 1
        pares.insert(p, lista[c])
    elif lista[c] % 2 == 1:
        impares.insert(q, lista[c])
        q += 1
print(f'Os pares da lista são {pares}')
print(f'Os ímpares da lista são {impares}')