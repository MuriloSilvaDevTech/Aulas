from datetime import date
nas = int(input('Ano de nascimento: '))
idade = date.today().year - nas
print('Quem nasceu em {} tem {} anos em {}.'.format(nas,idade,date.today().year))
if idade > 19:
    print('Você já deveria ter se alistado há {} anos.\nSeu alistamento foi em {}.'.format(idade - 18,nas + 18))
elif idade == 19:
    print('Você já deveria ter se alistado há 1 ano.\nSeu alistamento foi em {}.'.format(nas + 18))
elif idade == 18:
    print('Você está na idade certa para se alistar!')
elif nas > date.today().year:
    print('Idade inválida, por favor, tente novamente!')
else:
    print('Ainda faltam {} anos para você poder se alistar.\nVocê irá se alistar no ano de {}.'.format(18 - idade, nas + 18))