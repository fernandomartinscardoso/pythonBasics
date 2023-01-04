"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 28
   Programador: Fernando Martins Cardoso
"""

print('\033[31m###\033[m'*12)
print('\033[31m#\033[m\033[32mSoma dos quadrados de três números\033[m\033[31m#\033[m')
print('\033[31m###\033[m'*12)
n1 = float(input('\033[34mDigite o primeiro número: \033[m'))
n2 = float(input('\033[32mDigite o segundo número: \033[m'))
n3 = float(input('\033[36mDigite o terceiro número: \033[m'))
soma = n1**2 + n2**2 + n3**2
print('{}²+{}²+{}² = {:.1f}'.format(n1, n2, n3, soma))
