"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 56
   Programador: Fernando Martins Cardoso
"""
print('###'*23)
print('#                     Somador de números primos                     #'.upper())
print('#               Soma dos números primos menores que n               #')
print('###'*23)

n = int(input("Digite o valor de n: "))
while n <= 2:
    print("Número inválido. Tente novamente!")
    n = int(input("Digite o valor de n: "))

def primo(p):
    primo = True
    parada = int(p**0.5) +  1
    for i in range(2, parada):
        if p%i == 0:
            primo = False
            break
    return primo

numero = 2
soma = 0
while numero <= n:
    if primo(numero) == True:
        soma = soma + numero
    numero = numero + 1 

print('A soma dos números primos menores que {} é igual a {}.'.format(n,soma))