"""Gabarito da Lista 4 - Vetores e Matrizes
   Exercício 04
   Programador: Fernando Martins Cardoso
"""

print('#########################################################')
print('#     soma de dois valores de um vetor de 8 posições    #'.upper())
print('#########################################################')

print('Criando o vetor de oito posições:')
n = []
for i in range(1,9):
    a = input('Insira o {}° número: '.format(i))
    while ((a.strip('+-')).replace('.','')).isnumeric() == False:
        print('Entrada inválida. Insira um valor numérico.')
        a = input('Insira o {}° número: '.format(i))
    n.append(float(a))
print('Vetor criado: \n{}'.format(n))

print('\nInsira o valor das duas posições que você deseja somar:')
p1 = int(input('Insira a primeira posição: '))
while p1<1 or p1>8:
    print('Entrada inválida. Insira um valor entre 1 e 8.')
    p1 = int(input('Insira a primeira posição: '))

p2 = int(input('Insira a segunda posição: '))
while p2==p1 or p2<1  or p2>8:
    print('Entrada inválida. Insira um valor entre 1 e 8 diferente da primeira posição.')
    p2 = int(input('Insira a segunda posição: '))

soma = n[p1-1] + n[p2-1]

print('\nA soma dos elementos na posição {} e {} é igual a {:.2f}.'.format(p1,p2,soma))
