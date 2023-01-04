"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 30
   Programador: Fernando Martins Cardoso
"""

print('###'*11)
print('# Conversor de Real para Dólar  #')
print('###'*11)
print('\nQuantos reais você deseja converter para dólar?')
real = float(input('R$'))
print('Qual a cotação do dólar hoje?')
dolar = float(input('US$1.00 = R$'))
print('\nR${:.2f} = US${:.2f}'.format(real, real/dolar))
