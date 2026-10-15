from random import shuffle
a1 = input('O nome do primeiro aluno é: ')
a2 = input('O nome do segundo aluno é: ')
a3 = input('O nome do terceiro aluno é: ')
a4 = input('O nome do quarto aluno é: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será \n{}'.format(lista))