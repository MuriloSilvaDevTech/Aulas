from time import sleep
num = int(input('Digite um número qualquer: '))
print('--- ANALISANDO SE É PAR OU IMPAR ---')
sleep(2)
if num % 2 == 1:
    print('Seu número é IMPAR!')
else:
    print('Seu número é PAR!')