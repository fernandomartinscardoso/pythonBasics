"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 09
   Programador: Fernando Martins Cardoso
"""

print('###'*25)
print('#                    Avaliando pedido de empréstimo                       #'.upper())
print('#   Se a prestação do empréstimo exceder 20% do salário, negar o pedido.  #')
print('###'*25)

sal = float(input('Digite o valor do salário: R$'))
prest = float(input('Insira o valor da prestação: R$'))

if prest > 0.2*sal:
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")
