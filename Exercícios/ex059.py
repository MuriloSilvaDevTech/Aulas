from time import sleep
opcao = 0
maior = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    maior = n1
else:
    maior = n2
while opcao != 5:
    print('{:-^30}'.format(' MENU DE OPERAÇÕES '))
    opcao = int(input('[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR DO PROGRAMA\n>>>>>> QUAL É A SUA OPÇÃO? '))
    if opcao == 1:
        print('A soma dos números {} e {} é {}.'.format(n1, n2, n1 + n2))
        sleep(1)
    elif opcao == 2:
        print('A multriplicação dos números {} e {} é {}.'.format(n1, n2, n1 * n2))
        sleep(1)
    elif opcao == 3:
        print('O maior número entre {} e {} é o {}.'.format(n1, n2, maior))
        sleep(1)
    elif opcao == 4:
        print('Informe o valor novamente: ')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        sleep(1)
    elif opcao != 5:
        print('Opção inválida, tente novamente!')
