"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 20
   Programador: Fernando Martins Cardoso
"""

print('###'*18)
print('#               Avaliando triângulos                 #'.upper())
print('''#                       /\\                           #
#                      /  \\                          #
#                   A /    \\ B                       #
#                    /      \\                        #
#                   /________\\                       #
#                        C                           #''')
print('###'*18)

a = float(input('Digite o lado A: '))
b = float(input('Digite o lado B: '))
c = float(input('Digite o lado C: '))

if a>b+c or b>a+c or c>a+b:
    print('Os segmentos {}, {} e {} não formam um triângulo.'.format(a, b, c))
elif a==b and b==c:
    print('Os segmentos {}, {} e {} formam um triângulo equilátero.'.format(a, b, c))
elif a==b or a==c or b==c:
    print('Os segmentos {}, {} e {} formam um triângulo isósceles.'.format(a, b, c))
else:
    print('Os segmentos {}, {} e {} formam um triângulo escaleno.'.format(a, b, c))



