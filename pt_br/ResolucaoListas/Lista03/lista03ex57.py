"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 57
   Programador: Fernando Martins Cardoso
"""
print('###'*23)
print('#                    Contador de números primos                     #'.upper())
print('#            Conta quantos primos entre os números a e b            #')
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

cont = 0
a1 = a + 1
while a1 < b:
    if primo(a1) == True:
        cont = cont + 1
    a1 = a1 + 1

if cont == 0:
    print('Entre os números {} e {} não há número primo.'.format(a,b))
elif cont == 1:
    print('Entre os números {} e {} há {} número primo.'.format(a,b,cont))
else:
    print('Entre os números {} e {} há {} números primos.'.format(a,b,cont))