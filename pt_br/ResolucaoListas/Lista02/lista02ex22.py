"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 22
   Programador: Fernando Martins Cardoso
"""

print('###'*18)
print('#           Avaliação da aposentadoria               #'.upper())
print('#      Por Idade e Por Tempo de Contribuição         #')
print('###'*18)

idade = int(input('Insira a idade: '))
t = int(input('Insira o tempo de contribuição: '))

if idade>=65 or t>=30 or (idade>=60 and t>=25):
    print('Pode se aposentar!')
else:
    print('Não pode se aposentar!')