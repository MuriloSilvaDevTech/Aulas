maior18 = homem = mulherMenor20 = 0
while True:
    print('—' * 30)
    print(f'{'CADASTRE UMA PESSOA':^30}')
    print('—' * 30)
    idd = int(input('Idade: '))
    sex = ' '
    continuar = ' '
    while sex not in 'MF':
        sex = input('Sexo [M/F]: ').strip().upper()[0]
    print('—' * 30)
    while continuar not in 'SN':
        continuar = input('Quer continuar [S/N]: ').upper().strip()[0]
    if idd < 20 and sex == 'F':
        mulherMenor20 += 1
    if sex == 'M':
        homem += 1
    if idd > 18:
        maior18 += 1
    if continuar == 'N':
        break
print('—' * 30)
print(f'Total de pessoas maiores de 18 anos: {maior18}')
print(f'Total de homens cadastrados: {homem}')
print(f'Total de mulheres com menos de 20 anos cadastradas: {mulherMenor20}')
