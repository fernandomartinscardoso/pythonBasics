"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 25
   Programador: Fernando Martins Cardoso
"""

print('###'*18)
print('#          Resolvendo a equação do 2º grau           #'.upper())
print('###'*18)

print('\n Considere a equação na forma geral ax²+bx+c=0')
a = float(input('Insira o valor de a: '))
b = float(input('Insira o valor de b: '))
c = float(input('Insira o valor de c: '))

if a == 0:
    print('Não é equação de segundo grau porque a=0.')
else:
    delta = b**2-4*a*c
    if  delta < 0:
        print('Não existe raiz real!')
    elif delta == 0:
        x = -b/(2*a)
        print('Raízes iguais: x1 = x2 = {:.2f}'.format(x))
    else:
        x1 = (-b+(delta)**0.5)/(2*a)
        x2 = (-b-(delta)**0.5)/(2*a)
        print('Raízes distintas: x1 = {:.2f} e x2 = {:.2f}'.format(x1, x2))
