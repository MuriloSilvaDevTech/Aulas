kg = float(input('Qual é o seu peso? (Kg) '))
m = float(input('Qual é sua altura? (m) '))
imc = kg / m ** 2
print('Seu Índice de Massa Corpórea (IMC) é {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO ideal!')
elif imc >= 18.5 and imc < 25:
    print('Você está no PESO IDEAL!')
elif imc >= 25 and imc < 30:
    print('Você está em SOBREPESO!')
elif imc >= 30 and imc < 40:
    print('Você se encontra em OBESIDADE!')
else:
    print('Você se encontra em OBESIDADE MÓRBIDA, cuidado!!!')