from random import randint
computador = randint(0,5)
print('-=-' * 13)
print('Estou pensando em um número de 0 à 5...')
jogador = int(input('Tente adivinhar qual é este número: '))
print('-=-' * 13)
if jogador == computador:
    print('PARABÉNS!!! Eu pensei exatamente no número {} e você acertou!!!'.format(computador))
else:
    print('Não foi dessa vez... Eu escolhi o número {} e você escolheu o {}.'.format(computador,jogador))