from datetime import date
ano_atual = date.today().year
print('Alistamento Militar'.upper())
ano_nasc = int(input('Digite o ano de nascimento: '))
idade = ano_atual-ano_nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nasc, idade, ano_atual))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(18-idade))
    print('Seu alistamento será em {}.'.format(ano_atual+(18-idade)))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade-18))
    print('Seu ano de alistamento foi em {}'.format(ano_atual-(idade-18)))
else:
    print('Você deve se alistar imediatamente!')
