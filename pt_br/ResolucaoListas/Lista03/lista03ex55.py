"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 55
   Programador: Fernando Martins Cardoso
"""
print('###'*23)
print('#                     Somador de números primos                     #'.upper())
print('#                Soma dos n primeiros números primos                #')
print('###'*23)

n = int(input("Digite quantos números primos você gostaria de somar: "))
while n <= 1:
    print("Número inválido. Tente novamente!")
    n = int(input("Digite quantos números primos você gostaria de somar: "))

# Teste do algoritmo do Crivo de Eratóstenes