"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 58
   Programador: Fernando Martins Cardoso
"""
print('###'*23)
print('#                    Somador de números primos                      #'.upper())
print('#           Soma os números primos entre os números a e b           #')
print('###'*23)

a = int(input("Digite o valor de a: "))
while a < 1:
    print("Número inválido. Tente novamente!")
    a = int(input("Digite o valor de a: "))

b = int(input("Digite o valor de b: "))
while b <= a:
    print("Número inválido. Deve ser maior que a. Tente novamente!")
    b = int(input("Digite o valor de b: "))

def primo(p):
    primo = True
    parada = int(p**0.5) +  1
    for i in range(2, parada):
        if p%i == 0:
            primo = False
            break
    return primo

soma = 0
a1 = a + 1
while a1 < b:
    if primo(a1) == True:
        soma = soma + a1
    a1 = a1 + 1

print('A soma dos números primos entre os números {} e {} é igual a {}.'.format(a,b,soma))
