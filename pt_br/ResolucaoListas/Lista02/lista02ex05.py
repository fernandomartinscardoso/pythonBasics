"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 05
   Programador: Fernando Martins Cardoso
"""

print('\033[31mAvaliando se um número é\033[m \033[36mPAR\033[m \033[31mou\033[m \033[33mÍMPAR\033[m')
num = int(input('\033[34mDigite um número inteiro: \033[m'))
if num % 2 == 0:
    print('O número {} é par.'.format(num))
else:
    print('O número {} é ímpar.'.format(num))
