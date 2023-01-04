"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 29
   Programador: Fernando Martins Cardoso
"""

print('-+-'*15)
print('Este programa calcula a média de quatro notas'.upper())
print('-+-'*15)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
media = (n1 + n2 + n3 + n4)/4
print('A média das notas {:.1f}, {:.1f}, {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, n3, n4, media))