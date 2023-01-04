"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 19
   Programador: Fernando Martins Cardoso
"""

print('###'*19)
print('#    Extraindo algarismos de um número de 3 dígitos     #'.upper())
print('###'*19)

n = int(input('Insira um número de 3 dígitos: '))
# Teste para saber se o número inserido é de 3 dígitos:
while n<100 or n>999:
    print('Número inserido não é de 3 dígitos. Tente novamente!')
    n = int(input('Insira um número de 3 dígitos: '))

# Solução com string:
#n = str(n)
#for i in n:
#    print(i)
c = n
for i in range(0, 3):
    a = (c%1000)//100
    print(a)
    c = c*10