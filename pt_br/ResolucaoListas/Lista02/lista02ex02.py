"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 02
   Programador: Fernando Martins Cardoso
"""

print('###'*15)
print('#  Calculando a raiz quadrada de um número  #'.upper())
print('###'*15)

numero = float(input('Digite um número: '))
if numero < 0:
    print('Número inválido!')
else:
    raiz = numero**0.5
    print('A raiz quadrada de {} é igual a {:.2f}.'.format(numero, raiz))
