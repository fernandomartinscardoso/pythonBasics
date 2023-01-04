"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 27
   Programador: Fernando Martins Cardoso
"""

print('###'*11)
print('#     Categorias de natação     #'.upper())
print('###'*11)

idade = int(input('Digite a idade do(a) nadador(a): '))

if idade < 5:
    print('Não há categoria para esta idade!')
elif idade >= 5 and idade <= 7:
    print('Categoria: Infantil A')
elif idade > 7 and idade <= 10:
    print('Categoria: Infantil B')
elif idade > 10 and idade <= 13:
    print('Categoria: Juvenil A')
elif idade > 13 and idade <= 17:
    print('Categoria: Juvenil B')
else:
    print('Categoria: Sênior')