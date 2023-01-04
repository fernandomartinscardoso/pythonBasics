"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 39
   Programador: Fernando Martins Cardoso
"""

print('###'*23)
print('#       Cálculo da área de um triângulo pela base e a altura        #'.upper())
print('#        Base ou altura nulas ou negativas não são aceitas          #')
print('###'*23)

b = float(input('Digite o valor da base: '))
h = float(input('Digite o valor da altura: '))
while b<=0 or h<=0:
    print('Erro! Tanto a base quanto a altura precisam ser positivos.')
    print('Tente novamente!')
    b = float(input('Digite o valor da base: '))
    h = float(input('Digite o valor da altura: '))
area = (b*h)/2

print('A área do triângulo com altura {} e base {} é igual a {}.'.format(h, b, area))