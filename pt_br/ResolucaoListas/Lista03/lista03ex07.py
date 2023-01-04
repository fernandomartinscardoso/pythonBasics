"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 07
   Programador: Fernando Martins Cardoso
"""

print('###'*13)
print('#   Média de 10 inteiros positivos    #'.upper())
print('###'*13)

c = 1
s = 0
while c<=10:
    n = int(input('Digite o {}º número: '.format(c)))
    if n>0:
        s = s+n
        c = c+1
    else:
        print('Valor negativo inválido. Tente novamente!')
media = s/(c-1)
print('Média = {:.1f}'.format(media))
