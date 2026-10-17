from random import randint
comp = randint(0, 10)
c = 0
print('Sou seu computador!!!\nPensei em um número entre 0 e 10, consegue adivinhar?')
acertou = False
while not acertou:
    jog = int(input('Faça seu palpite: '))
    c += 1
    if jog < comp:
        print('Mais...', end=' ')
    elif jog > comp:
        print('Menos...',end=' ')
    else:
        acertou = True
print('Você acertou em {} tentativas, parabéns!!!'.format(c))