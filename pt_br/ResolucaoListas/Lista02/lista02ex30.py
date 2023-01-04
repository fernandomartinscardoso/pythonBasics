"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 30
   Programador: Fernando Martins Cardoso
"""

print('###'*13)
print('#   Três números em ordem crescente   #'.upper())
print('###'*13)
     
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a==b or a==c or b==c:
    print('Erro! Números repetidos foram inseridos.')
elif a<b and a<c:
    if b>c:
        print('Ordem crescente: {}, {} e {}'.format(a, c, b))
    else:
        print('Ordem crescente: {}, {} e {}'.format(a, b, c))
elif b<a and b<c:
    if a>c:
        print('Ordem crescente: {}, {} e {}'.format(b, c, a))
    else:
        print('Ordem crescente: {}, {} e {}'.format(b, a, c))
else:
    if a>b:
        print('Ordem crescente: {}, {} e {}'.format(c, b, a))
    else:
        print('Ordem crescente: {}, {} e {}'.format(c, a, b))
