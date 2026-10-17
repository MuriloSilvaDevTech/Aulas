print('{:=^40}'.format(' GERADOR DE PA '))
pri = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
quant = 0
tot = 0
ter = 10
c = 0
while ter != 0:
    tot += ter
    quant += ter
    while c <= tot:
        print('{}'.format(pri), end=' → ')
        pri += raz
        c += 1
    print('PAUSA')
    ter = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(quant))
