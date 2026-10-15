print('{:=^40}'.format(' LOJAS SILVA '))
valor = float(input('Digite o valor final da sua compra: R$'))
print('Ótimo! Sua compra deu R${:.2f}, escolha a opção que deseja a seguir: '.format(valor))
print('[ 1 ] PAGAMENTO À VISTA (DINHEIRO/CHEQUE)\n[ 2 ] PAGAMENTO NO DÉBITO (CARTÃO)\n[ 3 ] PAGAMENTO NO CRÉDITO (CARTÃO)')
opcao = int(input('Qual é a sua opcão? '))
if opcao == 1:
    print('Sua compra no valor de R${:.2f} ficará em R${:.2f} com o desconto à vista no dinheiro/cheque!'.format(valor, valor * 0.9))
elif opcao == 2:
    print('Sua compra no valor de R${:.2f} ficará em R${:.2f} com o desconto no débito!'.format(valor, valor * 0.95))
elif opcao == 3:
    parc = int(input('Será dividido em quantas parcelas? '))
    if parc == 1:
        print('Sua compra ficará no valor de R${:.2f}!'.format(valor))
    elif parc == 2:
        print('Sua compra ficará no valor de R${:.2f} dividido em {} vezes de R${:.2f}!'.format(valor,parc,valor / parc))
    elif parc <= 0:
        print('Opção inválida!')
    else:
        print('Sua compra ficará no valor de R${:.2f} dividido em {} vezes de R${:.2f}!'.format(valor * 1.2,parc,valor * 1.2 / parc))
else:
    print('Opção inválida, tente novamente.')
print('OBRIGADO PELA PREFERÊNCIA!\nVOLTE SEMPRE!')