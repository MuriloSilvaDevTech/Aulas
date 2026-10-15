from datetime import date
maior = 0
menor = 0
for ano in range(1, 8):
    idd = int(input('Em que ano a {}° pessoa nasceu? '.format(ano)))
    if idd < date.today().year - 18:
        menor += 1
    else:
        maior += 1
print('Nesta listagem possue {} pessoas maiores de idade e {} pessoas menores de idade.'.format(maior, menor))