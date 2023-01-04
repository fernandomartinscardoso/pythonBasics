"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 32
   Programador: Fernando Martins Cardoso
"""

print('###'*13)
print('#         Caixa de Lanchonete         #'.upper())
print('###'*13)

print('''Tabela do cardápio:
    
Especificação    | Código |  Preço
_________________|________|________
Cachorro Quente  |   100  |  1.20
Bauru Simples    |   101  |  1.30
Bauru com Ovo    |   102  |  1.50
Hamburguer       |   103  |  1.20
Cheeseburguer    |   104  |  1.70
Suco             |   105  |  2.20
Refrigerante     |   106  |  1.00
    
''')

cod = int(input('Digite o código do produto: '))
quant = int(input('Informe a quantidade de itens:'))

if cod == 100:
    total = quant*1.2
    print('''\nItem                Quantidade
Cachorro quente         {}
------------------------------
Total a pagar       R$ {:.2f}'''.format(quant, total))
elif cod == 101:
    total = quant*1.3
    print('''\nItem                Quantidade
Bauru simples           {}
------------------------------
Total a pagar       R$ {:.2f}'''.format(quant, total)) 
elif cod == 102:
    total = quant*1.5
    print('''\nItem                Quantidade
Bauru com ovo           {}
------------------------------
Total a pagar       R$ {:.2f}'''.format(quant, total))
elif cod == 103:
    total = quant*1.2
    print('''\nItem                Quantidade
Hamburguer              {}
------------------------------
Total a pagar       R$ {:.2f}'''.format(quant, total))
elif cod == 104:
    total = quant*1.7
    print('''\nItem                Quantidade
Cheeseburguer           {}
------------------------------
Total a pagar       R$ {:.2f}'''.format(quant, total))
elif cod == 105:
    total = quant*2.2
    print('''\nItem                Quantidade
Suco                    {}
------------------------------
Total a pagar       R$ {:.2f}'''.format(quant, total))
elif cod == 106:
    total = quant*1.0
    print('''\nItem                Quantidade
Refrigerante            {}
------------------------------
Total a pagar       R$ {:.2f}'''.format(quant, total))
else:
    print('Código de produto inválido!')