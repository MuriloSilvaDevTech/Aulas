nome=input('Digite seu nome completo: ').strip().split()
print('Prazer em te conhecer!\nSeu primeiro nome é {}.\nSeu último nome é {}.'.format(nome[0], nome[len(nome)-1]))