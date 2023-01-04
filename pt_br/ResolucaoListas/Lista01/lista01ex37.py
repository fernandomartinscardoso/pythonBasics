"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 37
   Programador: Fernando Martins Cardoso
"""

print('###'*18)
print('#  Aplicando Desconto de 12% no Preço de um Produto  #')
print('###'*18)
preco = float(input('Digite o valor do produto: R$'))
desconto = preco*((100-12)/100)
print('Com desconto de 12%, o produto custará R${:.2f}.'.format(desconto))
