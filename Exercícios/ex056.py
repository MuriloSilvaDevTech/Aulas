media = 0
maior = 0
m = 0
velho = ''
for p in range(1, 5):
    print('{:-^25}'.format(' {}° PESSOA').format(p))
    nome = input('Nome: ').title().strip()
    idd = int(input('Idade: '))
    sex = input('Sexo [M/F]: ').upper().strip()
    media += idd
    if sex == 'F' and idd < 20:
        m += 1
    if idd > maior and sex == 'M':
        maior = idd
        velho = nome
print('-' * 40)
print('A média de idade do grupo é de {:.1f} anos.'.format(media / p))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(m))
