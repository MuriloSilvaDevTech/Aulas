sex = input('Digite seu sexo [M/F]: ').strip().upper()[0]
while sex not in 'MF':
    sex = input('Dados inválidos. Por favor, informe seu Sexo [M/F]: ').strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sex))