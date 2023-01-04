from datetime import date
print('='*42)
print('Descubra se um determinado ano é bissexto!')
print('='*42)
ano = int(input('Digite o ano a ser analisado (digite 0 para o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 400 == 0 or ano % 100 != 0 and ano % 4 == 0:
    print('O ano de {} é bissexto.'.format(ano))
else:
    print('O ano de {} não é bissexto.'.format(ano))
