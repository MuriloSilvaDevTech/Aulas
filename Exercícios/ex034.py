sal = float(input('Digite seu salário atual: '))
if sal > 1250:
    print('Após o aumento, seu salário de {:.2f} será alterado para {:.2f}!'.format(sal,sal*1.1))
else:
    print('Após o aumento, seu salário de {:.2f} será alterado para {:.2f}!'.format(sal,sal*1.15))