"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 52
   Programador: Fernando Martins Cardoso
"""
print('###'*23)
print('#                          caixa eletrônico                         #'.upper())
print('#  Separar o valor de saque em notas de 100, 50, 20, 10, 5, 2 e 1   #')
print('###'*23)

valor = float(input('Insira o valor de saque: R$ '))
while valor%1 != 0:
    print('Valor inválido. Só é permitido valores inteiros.')
    valor = float(input('Insira o valor de saque: R$'))
valor_inicial = valor

nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0

while valor >= 100:
    valor = valor - 100
    nota100 = nota100 + 1

while valor >= 50:
    valor = valor - 50
    nota50 = nota50 + 1

while valor >= 20:
    valor = valor - 20
    nota20 = nota20 + 1

while valor >= 10:
    valor = valor - 10
    nota10 = nota10 + 1

while valor >= 5:
    valor = valor - 5
    nota5 = nota5 + 1

while valor >= 2:
    valor = valor - 2
    nota2 = nota2 + 1

while valor >= 1:
    valor = valor - 1
    nota1 = nota1 + 1

print("Para sacar R$ {:.2f} são necessárias: \n* {} notas de 100 \n* {} notas de 50 \n* {} notas de 20 \n* {} notas de 10 \n* {} notas de 5 \n* {} notas de 2 \n* {} notas de 1 ".format(valor_inicial, nota100, nota50, nota20, nota10, nota5, nota2, nota1))
