from random import randint
cont = 0
print('—' * 40)
print(f'{'VAMOS JOGAR PAR OU ÍMPAR':^40}')
print('—' * 40)
while True:
    comp = randint(0, 10)
    jog = int(input('Digite um valor: '))
    escolha = input('Par ou ímpar [P/I]? ').upper().strip()[0]
    result = (jog + comp) % 2
    print('=' * 40)
    if escolha not in 'PI':
        print('Escolha inválida, tente novamente!')
    else:
        if result == 1:
            print(f'Você jogou {jog} e o computador {comp}. Total de {jog + comp} - DEU IMPAR')
            if escolha == 'I':
                print('Você VENCEU!\nVamos jogar novamente...')
                cont += 1
            elif escolha == 'P':
                print('Você PERDEU!')
                break
        elif result % 2 == 0:
            print(f'Você jogou {jog} e o computador {comp}. Total de {jog + comp} - DEU PAR')
            if escolha == 'I':
                print('Você PERDEU!')
                break
            elif escolha == 'P':
                print('Você VENCEU!\nVamos jogar novamente...')
                cont += 1
    print('=' * 40)
print(f'GAME OVER! Você venceu {cont} vezes.')