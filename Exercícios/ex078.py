valores = []
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {v}: ')))
print('—' * 35)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ',end='')
for i, c, in enumerate(valores):
    if valores[i] == max(valores):
        print(f'{i}...', end=' ')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for i, c in enumerate(valores):
    if valores[i] == min(valores):
        print(f'{i}...', end=' ')