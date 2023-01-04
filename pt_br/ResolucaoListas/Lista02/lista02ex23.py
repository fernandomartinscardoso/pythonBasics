"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 23
   Programador: Fernando Martins Cardoso
"""

print('###'*18)
print('#          Avaliando se um ano é bissexto            #'.upper())
print('###'*18)

ano = int(input('Insira o ano a ser avaliado: '))

if ano%400==0 or (ano%4==0 and ano%100!=0):
    print('O ano de {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
