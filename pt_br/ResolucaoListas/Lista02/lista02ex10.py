"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 10
   Programador: Fernando Martins Cardoso
"""

print('###'*22)
print('#    Peso ideal para homens e mulheres de acordo com a altura    #'.upper())
print('###'*22)

h = float(input('Insira a altura: '))
s = str(input('Insira o sexo (M ou F): '))
if s == 'M':
    peso = 72.7*h - 58
    print('O peso ideal de um homem de {:.2f} m é igual a {:.1f} kg.'.format(h, peso))
elif s == 'F':
    peso = 62.1*h - 44.7
    print('O peso ideal de uma mulher de {:.2f} m é igual a {:.1f} kg.'.format(h, peso))
else:
    print('Opção inválida.')
