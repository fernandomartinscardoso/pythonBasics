"""Gabarito da Lista 4 - Vetores e Matrizes
   Exercício 05
   Programador: Fernando Martins Cardoso
"""

print('#########################################################')
print('#      leitura de 10 números e separação dos pares      #'.upper())
print('#########################################################')

print('Lendo os dez números e armazenando num vetor:')
n = []
for i in range(1,11):
    a = input('Insira o {}° número: '.format(i))
    while (a.strip('+-')).isnumeric() == False:
        print('Entrada inválida. Insira um número inteiro.')
        a = input('Insira o {}° número: '.format(i))
    n.append(int(a))
print('Vetor criado: \n{}'.format(n))

pares = []
for j in n:
    if j%2 == 0:
        pares.append(j)
if len(pares)==0:
    print('Não foi inserido nenhum número par.')
elif len(pares)==1:
    print('Só um par foi inserido. É ele o número {}.'.format(pares[0]))
else:
    print('Dos números inseridos {} são pares. São eles: {}'.format(len(pares),pares))
