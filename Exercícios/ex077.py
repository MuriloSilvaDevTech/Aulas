palavras = ('APRENDER', 'PROGRAMAR', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
cont = 0
for n in palavras:
    print(f'com o total de {cont} vogais.\nNa palavra {n} temos ', end='')
    cont = 0
    for letra in n:
        if letra in 'AEIOU':
            cont += 1
            print(letra, end=' ')
print(f'com o total de {cont} vogais.')