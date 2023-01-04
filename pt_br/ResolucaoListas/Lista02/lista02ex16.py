"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 16
   Programador: Fernando Martins Cardoso
"""

print('###'*17)
print('#       Número correspondente ao mês do ano       #'.upper())
print('#     1-Janeiro, 2-Fevereiro,..., 12-Dezembro     #')
print('###'*17)

n = int(input('Digite um número de 1 a 12: '))
if n == 1:
    print('Janeiro')
elif n == 2:
    print('Fevereiro')
elif n == 3:
    print('Março')
elif n == 4:
    print('Abril')
elif n == 5:
    print('Maio')
elif n == 6:
    print('Junho')
elif n == 7:
    print('Julho')
elif n == 8:
    print('Agosto')
elif n == 9:
    print('Setembro')
elif n == 10:
    print('Outubro')
elif n == 11:
    print('Novembro')
elif n == 12:
    print('Dezembro')
else:
    print('Opção inválida!')
