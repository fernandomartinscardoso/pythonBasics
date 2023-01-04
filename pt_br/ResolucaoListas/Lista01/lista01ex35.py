"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 35
   Programador: Fernando Martins Cardoso
"""

print('###'*14)
print('#  Hipotenusa de um Triângulo Retângulo  #')
print('###'*14)
c1 = float(input('Digite o valor do primeiro cateto: '))
c2 = float(input('Digite o valor do segundo cateto: '))
hip = (c1**2 + c2**2)**(1/2)
print('O triângulo retângulo cujos catetos são {} e {}, tem hipotenusa igual a {:.2f}.'.format(c1, c2, hip))
