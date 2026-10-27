lista = []
while True:
    lista.append(input('Digite um valor: '))
    opcao = input('Quer continuar? [S/N] ').upper().strip()[0]
    if opcao in 'N':
        break
lista.sort(reverse=True)
print('—' * 30)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:print('A lista contém o valor 5!')
else:print('O valor 5 não foi encontrado na lista!')
