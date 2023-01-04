"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 08
   Programador: Fernando Martins Cardoso
"""

print('###'*13)
print('#  Calculando a média de duas notas   #'.upper())
print('#   Avaliando a validade das notas    #')
print('###'*13)

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
if nota1<0 or nota1>10 or nota2<0 or nota2>10:
    print('Valor inválido para uma das notas!')
    print('Só são válidas notas entre 0 e 10.')
else:
    media = (nota1 + nota2)/2
    print('Média = {:.1f}'.format(media))
