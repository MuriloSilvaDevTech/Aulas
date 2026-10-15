dias=int(input('Quantos dias foram alugados? '))
km=float(input('Quantos quilometros foram percorridos? '))
valorDias= dias*60
valorKm= km*0.15
print('O total a pagar é de R${:.2f}.'.format(valorDias+valorKm))