palavra = input('Digite uma frase: ').strip().upper().split()
frase = ''.join(palavra)
inverso = ''
for c in range(len(frase) - 1, -1, -1):
    inverso += frase[c]
    print('O inverso de {} é {}.'.format(frase, inverso))
if inverso == frase:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')