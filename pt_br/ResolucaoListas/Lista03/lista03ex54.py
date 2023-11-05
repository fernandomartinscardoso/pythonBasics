"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 54
   Programador: Fernando Martins Cardoso
"""
print('###'*23)
print('#                      Detector de número primo                     #'.upper())
print('#    Recebe um número inteiro maior que 1 e testa se ele é primo    #')
print('###'*23)

n = int(input("Digite um número inteiro maior que 1: "))
while n <= 1:
    print("Número inválido. Tente novamente!")
    n = int(input("Digite um número inteiro maior que 1: "))

primo = True
parada = int(n**(0.5)) + 1

for i in range(2,parada):
    if n % i == 0:
        primo = False
        break

if primo == True:
    print('O número {} é primo'.format(n))
else:
    print('O número {} não é primo'.format(n))