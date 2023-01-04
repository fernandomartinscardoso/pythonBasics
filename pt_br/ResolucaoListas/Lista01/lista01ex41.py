"""Gabarito da Lista 1 - Variáveis e Expressões
   Exercício 41
   Programador: Fernando Martins Cardoso
"""

print('###'*20)
print('#          Pagamento de salário de um funcionário          #'.upper())
print('# Inserir o valor da hora de trabalho e horas trabalhadas  #'.upper())
print('###'*20)
vht = float(input('Digite o valor da hora de trabalho: R$'))
horas = float(input('Digite o número de horas trabalhadas no mês: '))
sal = vht*horas
sal10 = sal + (10/100)*sal
print('Com bonificação de 10%, o salário a ser pago é de \033[34mR${:.2f}\033[m.'.format(sal10))
