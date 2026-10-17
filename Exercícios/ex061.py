print('{:=^30}'.format(' GERADOR DE PA '))
ter = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
c = 0
while c < 10:
    print('{}'.format(ter), end=' → ')
    ter += raz
    c += 1
print('Acabou!')