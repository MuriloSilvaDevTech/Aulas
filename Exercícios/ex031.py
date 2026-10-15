km = int(input('Qual é a distância da sua viagem? '))
print('O valor promocional da passagem para além de 200Km é R$0,45!')
print('Você está prestes a começar uma viagem de {:.1f}Km'.format(km))
if km <= 200:
    print('O valor da passagem é de R${:.2f}.'.format(km * 0.5))
else:
    print('O valor da sua passagem custa R${:.2f}.\nObrigado por viajar conosco!'.format(km * 0.45))