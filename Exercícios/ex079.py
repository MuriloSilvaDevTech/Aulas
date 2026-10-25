valores = []
while True:
    novo = (int(input('Digite um valor: ')))
    if novo not in valores:
        valores.append(novo)
    else:
        print('Valor duplicado! Não adicionarei a lista...')
    opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
    while opcao not in 'SN':
        print('Opção inválida!')
        opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
    if opcao == 'N':
        break
print('—' * 35)
print(f'Você digitou os valores {valores}')