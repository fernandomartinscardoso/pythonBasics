"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 32
   Programador: Fernando Martins Cardoso
"""

print('###'*16)
print('''#  Soma do antecessor do triplo com o sucessor #
#  do dobro de um número inteiro               #''')
print('###'*16)
n = int(input('Digite um número inteiro: '))
at = 3*n - 1
sd = 2*n + 1
soma = at + sd
print('A soma do antecessor do triplo de {} com o sucessor de seu dobro é igual a {}.'.format(n, soma))
