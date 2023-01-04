"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 09
   Programador: Fernando Martins Cardoso
"""

print('###'*17)
print('#   Imprimindo os N primeiros naturais ímpares    #'.upper())
print('###'*17)

N = int(input('Quantos ímpares deseja gerar?\n'))
print('Os {} primeiros naturais ímpares são:'.format(N))
for i in range(0, N):
    print(2*i+1)
