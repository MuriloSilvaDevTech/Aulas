while True:
    print('—' * 35)
    print(f'{'TABUADA':^35}')
    print('—' * 35)
    val = int(input('Digite o número que deseja ver na tabuada: '))
    if val < 0:
        break
    for i in range(1, 11):
        print(f'{val} x {i:2} = {val * i}')
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')