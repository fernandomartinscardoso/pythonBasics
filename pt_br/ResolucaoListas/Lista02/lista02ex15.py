"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 15
   Programador: Fernando Martins Cardoso
"""

print('###'*17)
print('#      Número correspondente ao dia da semana     #'.upper())
print('#     1-Domingo, 2-Segunda-feira,..., 7-Sábado    #')
print('###'*17)

n = int(input('Digite um número de 1 a 7: '))
if n == 1:
    print('Domingo')
elif n == 2:
    print('Segunda-feira')
elif n == 3:
    print('Terça-feira')
elif n == 4:
    print('Quarta-feira')
elif n == 5:
    print('Quinta-feira')
elif n == 6:
    print('Sexta-feira')
elif n == 7:
    print('Sábado')
else:
    print('Opção inválida!')
