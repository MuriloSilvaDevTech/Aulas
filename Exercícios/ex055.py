maior = 0
menor = 0
for p in range(1, 6):
    kg = float(input('Quanto pesa a {}° pessoa? '.format(p)))
    if p == 1:
        maior = kg
        menor = kg
    else:
        if kg > maior:
            maior = kg
        elif kg < menor:
            menor = kg
print('O maior peso lido foi de {}Kg e o menor peso lido foi de {}Kg.'.format(maior, menor))