"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 52
   Programador: Fernando Martins Cardoso
"""

print('###'*16)
print('#   cercando um terreno retangular com tela    #'.upper())
print('###'*16)
c = float(input('Digite o comprimento do terreno (em m): '))
l = float(input('Digite a largura do terreno (em m): '))
p = 2*c + 2*l
pmt = float(input('Digite o preço do metro de tela: R$'))
print('O terreno tem {} m de perímetro e será necessário comprar R${:.2f} em tela para cercá-lo.'.format(p, p*pmt))
