opcao = ''
cont = media = maior = menor = 0
while opcao != 'N':
    n = int(input('Digite um número: '))
    opcao = input('Quer continuar [S/N] ? ').upper().strip()[0]
    cont += 1
    media += n
    if opcao != 'N':
        if opcao != 'S':
            print('Opção inválida, tente novamente!')
    if cont == 1:
        maior = menor = n
    else:
        if maior < n:
            maior = n
        elif menor > n:
            menor = n
print('Você digitou {} números e a média foi {:.2f}.'.format(cont, media / cont))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
