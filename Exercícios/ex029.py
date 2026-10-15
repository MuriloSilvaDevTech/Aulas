vel = float(input('Digite qual a velocidade do carro: '))
print('--- VELOCIDADE MÁXIMA DA VIA 80Km/h ---')
if vel > 80:
    print('Excesso de velocidade ultrapassado!\nVocê será multado e terá que pagar a multa no valor de R${:.2f}.'.format((vel - 80) * 7))
else:
    print('Velocidade dentro da regulamentação, tenha um bom dia!')