print('—' * 40)
print(f'{' BANCO MSDT ':^40}')
print('—' * 40)
ced100 = ced50 = ced25 = ced10 = ced5 = ced1 = 0
valor = int(input('Qual o valor que você deseja sacar? R$'))
while True:
    while True:
        if valor > 99:
            valor -= 100
            ced100 += 1
        elif valor > 49:
            valor -= 50
            ced50 += 1
        elif valor > 24:
            valor -= 25
            ced25 += 1
        elif valor > 9:
            valor -= 10
            ced10 += 1
        elif valor > 4:
            valor -= 5
            ced5 += 1
        elif valor > 0:
            valor -= 1
            ced1 += 1
        else:
            break
    break
ced100 = str(ced100).split(".")[0]
cel50 = str(ced50).split(".")[0]
cel25 = str(ced25).split(".")[0]
ced10 = str(ced10).split(".")[0]
ced5 = str(ced5).split(".")[0]
ced1 = str(ced1).split(".")[0]
print(f'Total de cédulas de 100: {ced100}')
print(f'Total de cédulas de 50: {ced50}')
print(f'Total de cédulas de 25: {ced25}')
print(f'Total de cédulas de 10: {ced10}')
print(f'Total de cédulas de 5: {ced5}')
print(f'Total de cédulas de 1: {ced1}')
