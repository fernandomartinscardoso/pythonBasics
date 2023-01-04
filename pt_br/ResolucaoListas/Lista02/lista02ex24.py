"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 24
   Programador: Fernando Martins Cardoso
"""

print('###'*18)
print('#             Avaliando imposto estatal              #'.upper())
print('###'*18)

v = float(input('Insira o valor do produto: R$'))
e = str(input('Insira o estado onde será vendido o produto (SP, MG, RJ ou MS): \n'))
if e == 'MG':
    p = v*1.07  # p é o preço do produto no estado, depois da aplicação do imposto
    print('Preço do produto em {} é igual a R${:.2f}.'.format(e, p))
elif e == 'SP':
    p = v*1.12
    print('Preço do produto em {} é igual a R${:.2f}.'.format(e, p))
elif e == 'RJ':
    p = v*1.15
    print('Preço do produto em {} é igual a R${:.2f}.'.format(e, p))
elif e == 'MS':
    p = v*1.08
    print('Preço do produto em {} é igual a R${:.2f}.'.format(e, p))
else:
    print('Opção inválida!')
