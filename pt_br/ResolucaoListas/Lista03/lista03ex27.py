"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 27
   Programador: Fernando Martins Cardoso
"""

print('###'*17)
print('#     Cálculo do número harmônico com n termos    #'.upper())
print('#            H(n)=1+1/2+1/3+1/4+...+1/n           #')
print('###'*17)

hn = 0
n = int(input('Insira o número n de termos: '))

# Verificando se o n é válido:
while n <= 0:
    print('Número inválido! O valor de n deve ser inteiro e positivo.')
    n = int(input('Insira o número n de termos: '))

for i in range(1, n+1):
    hn = hn + 1/i
print('H({}) = {}'.format(n, hn))
