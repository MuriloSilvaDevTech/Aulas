frase = input('Digite uma frase: ').strip().upper()
print('A frase mostra a letra A em {} vezes.'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}.'.format(frase.find('A')+1))
print('A última letra A da frase aparece na posiçao {}.'.format(frase.rfind('A')+1))