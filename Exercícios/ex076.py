lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90,
         'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('—' * 42)
print(f'{'LISTA DE PREÇOS':^42}')
print('—' * 42)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<32}', end='')
    elif pos % 2 == 1:
        print(f' R${lista[pos]:.2f}')
print('—' * 42)