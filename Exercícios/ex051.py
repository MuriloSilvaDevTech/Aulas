print('{:=^40}'.format(' 10 TERMOS DE UMA PA '))
ter = int(input('Digite o termo da sua PA: '))
r = int(input('Digite a razão da sua PA: '))
for n in range (1, 11):
    print('{}'.format(ter), end=' → ')
    ter += r
print('ACABOU')