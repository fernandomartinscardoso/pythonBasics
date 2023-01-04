from datetime import date

print('###'*13)
print('# Classificação de Atletas da Natação #'.upper())
print('###'*13)

ano = int(input('Qual o ano de nascimento do atleta? '))
idade = date.today().year - ano
print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <=14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')

