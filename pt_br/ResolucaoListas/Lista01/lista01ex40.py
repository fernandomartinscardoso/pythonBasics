"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 40
   Programador: Fernando Martins Cardoso
"""

print('###'*20)
print('#           Pagamento de diárias de um encanador           #'.upper())
print('# R$30,00 por dia de trabalho e desconto de 8% de imposto  #'.upper())
print('###'*20)
dias = int(input('Quantos dias o encanador trabalhou? '))
pag = (dias*30)*(92/100)
print('O encanador deve receber R${:.2f}'.format(pag))
