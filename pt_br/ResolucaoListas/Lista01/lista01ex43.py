"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 43
   Programador: Fernando Martins Cardoso
"""

print('###'*16)
print('#              Programa de vendas              #'.upper())
print('#  Cálculo de descontos, parcelas e comissões  #'.upper())
print('###'*16)
v_prod = float(input('Digite o valor do produto: R$'))
avista = v_prod*(90/100)
parcela = v_prod/3
com_avista = avista*(5/100)
com_aprazo = v_prod*(5/100)
print('Preço do produto com desconto a vista: R${:.2f}'.format(avista))
print('Valor da parcela (venda a prazo em 3 vezes sem juros): R${:.2f}'.format(parcela))
print('Comissão para venda a vista: R${:.2f}'.format(com_avista))
print('Comissão para venda a prazo: R${:.2f}'.format(com_aprazo))
