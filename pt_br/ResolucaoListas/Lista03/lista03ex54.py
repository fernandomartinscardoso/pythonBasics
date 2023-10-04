"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 54
   Programador: Fernando Martins Cardoso
"""
print('###'*23)
print('#                      Detector de número primo                     #'.upper())
print('#    Recebe um número inteiro maior que 1 e testa se ele é primo    #')
print('###'*23)

n = int(input("Digite um número inteiro maior que 1:"))
while n <= 1:
    print("Número inválido. Tente novamente!")
    n = int(input("Digite um número inteiro maior que 1:"))

teste = n//2
cont = 1

while cont <= teste:
    cont = cont + 1
    if n % cont == 0:
        print("{} não é um número primo".format(n))
        break
    if cont > teste:
        print("{} é um número primo".format(n))


