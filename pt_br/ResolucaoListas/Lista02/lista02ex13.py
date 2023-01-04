"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 13
   Programador: Fernando Martins Cardoso
"""

print('###'*17)
print('#      Média ponderada de 3 notas e aprovação     #'.upper())
print('#   Este programa trabalha com notas de 0 a 100   #')
print('###'*17)

print('\nCondição de aprovação: média igual ou superior a 60 pontos.')
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
n3 = float(input('Insira a terceira nota: '))
media = (n1 + n2 + 2*n3)/4
print('Média = {:.1f}'.format(media))

if media >= 60:
    print('Aprovado')
else:
    print('Reprovado')