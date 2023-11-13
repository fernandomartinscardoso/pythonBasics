"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 60
   Programador: Fernando Martins Cardoso
"""
print('###'*23)
print('#                        Análise de números                         #'.upper())
print('#                 Soma e média de números digitados                 #')
print('###'*23)

cont = 1
soma = 0
cont_par = 1
soma_par = 0
maior_numero = 0
while True:
    numero = input('Insira o {}° número ou x para terminar: '.format(cont))
    if numero == 'x':
        break
    else:
        numero = float(numero)
    if cont == 1:
        menor_numero = numero
    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero
    if numero%2 == 0:
        soma_par = soma_par + numero
        cont_par = cont_par + 1
    soma = soma + numero
    cont = cont + 1

if cont==1:
    media = 0
    menor_numero = maior_numero
else:
    media = soma/(cont-1)

if cont_par==1:
    media_par = 0
else:
    media_par = soma_par/(cont_par-1)

print('A soma dos números digitados é igual a: {}'.format(soma))
print('A quantidade de número digitados é igual a: {}'.format(cont-1))
print('A média dos números digitados é igual a: {}'.format(media))
print('O maior número digitado é igual a: {}'.format(maior_numero))
print('O menor número digitado é igual a: {}'.format(menor_numero))
print('A média dos números pares é igual a: {}'.format(media_par))
