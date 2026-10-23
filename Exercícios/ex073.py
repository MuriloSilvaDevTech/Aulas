times = ('Flamengo', 'Palmeiras', 'Athlético-PR', 'Cruzeiro', 'Fluminense', 'Atlético-MG',
         'Bahia', 'Santos', 'São Paulo', 'Bragantino', 'Botafogo', 'Coritiba', 'EC Vitória', 'Mirassol',
         'Vasco da Gama', 'Corinthians', 'Internacional', 'Grêmio', 'Remo', 'Chapecoense')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são: {times[:5]}')
print('-=' * 30)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 30)
print(f'O Chapecoense está na {times.index('Chapecoense')+1}° posição.')