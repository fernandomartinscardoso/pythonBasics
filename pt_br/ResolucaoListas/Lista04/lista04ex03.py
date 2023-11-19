"""Gabarito da Lista 4 - Vetores e Matrizes
   Exercício 03
   Programador: Fernando Martins Cardoso
"""

print('#########################################################')
print('#   calculando e armazenando o quadrado de 10 números   #'.upper())
print('#########################################################')

n = []
for i in range(1,11):
    a = input('Insira o {}° número: '.format(i))
    while ((a.strip('+-')).replace('.','')).isnumeric() == False:
        print('Entrada inválida. Insira um valor numérico.')
        a = input('Insira o {}° número: '.format(i))
    n.append(float(a))

q = []
for j in n:
    q.append(j**2)

print('Valores inseridos: \n{}'.format(n))
print('Quadrado dos valores inseridos: \n{}'.format(q))
