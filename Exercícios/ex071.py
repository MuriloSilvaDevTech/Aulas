print('—' * 40)
print(f'{' BANCO MSDT ':^40}')
print('—' * 40)
valor = int(input('Qual o valor que você deseja sacar? R$'))
total = valor
ced = 100
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}.')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 25
        elif ced == 25:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totalced = 0
        if total == 0:
            break