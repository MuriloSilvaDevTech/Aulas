numeros = (int(input('Digite o 1° número: ')),
           int(input('Digite o 2° número: ')),
           int(input('Digite o 3° número: ')),
           int(input('Digite o 4° número: ')))
print(f'Você digitou os valores {numeros}.')
print(f'O número 9 foi digitado {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O primeiro número 3 foi escrito na {numeros.index(3)+1}° posição.')
else:
    print('O número 3 não foi digitado.')
print(f'Os números pares digitados foram .',end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end='')