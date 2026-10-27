numeros = []
for c in range(0, 5):
    novo = int(input('Digite um valor: '))
    if c == 0 or novo > numeros[-1]:
        numeros.append(novo)
        print('Número adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if novo <= numeros[pos]:
                numeros.insert(pos, novo)
                print(f'Numero adicionado na posição {numeros.index(novo)} da lista...')
                break
            pos += 1
print(numeros)