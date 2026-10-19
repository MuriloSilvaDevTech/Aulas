print('—' * 40)
print(f'{'LOJAS SILVA DEV':^40}')
print('—' * 40)
mais1000 = maior = menor = tot = cont = 0
maiorProduto = menorProduto = ''
while True:
    produto = input('Nome do pruduto: ').strip().title()
    preco = float(input('Preço: R$'))
    continuar = ' '
    tot += preco
    cont += 1
    if preco > 1000:
        mais1000 += 1
    if maior < preco:
        maior = preco
        maiorProduto = produto
        if cont == 1:
            menor = maior
            menorProduto = produto
    if menor > preco:
        menorProduto = produto
        menor = preco
    while continuar not in 'SN':
        continuar = input('Deseja continuar[S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'{' FIM DO PROGRAMA ':—^40}')
print(f'O total da compra foi de R${tot:.2f} com {cont} produtos, agradecemos a preferência!')
print(f'Nesta compra a quantidade de produtos que ultrapassaram o valor de R$1000,00 foram: {mais1000}')
print(f'O produto mais barato da lista foi {menorProduto} custando {menor:.2f}, enquanto o mais caro foi {maiorProduto} custando {maior:.2f}.')