valor=float(input('Qual o valor da casa? R$'))
salario=float(input('Qual o seu salário atual? R$'))
anos=int(input('Em quantos anos de financiamento? '))
prestacao=valor/(anos*12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(valor,anos,prestacao))
if prestacao >= salario*0.30:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')