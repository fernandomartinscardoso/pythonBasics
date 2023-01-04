"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 18
   Programador: Fernando Martins Cardoso
"""

print('###'*18)
print('#               Calculadora básica                   #'.upper())
print('#      Resolve as quatro operações fundamentais      #')
print('###'*18)

print('''Digite uma das opções abaixo:
SOM - para realizar a soma de dois números
SUB - para realizar a subtração de dois números
MUL - para realizar a multiplicação de dois números
DIV - para realizar a divisão de dois números ''')
escolha = str(input('Digite a opção desejada: '))

if escolha == 'SOM':
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    soma = n1 + n2
    print('Soma = {}'.format(soma))
elif escolha == 'SUB':
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    sub = n1 - n2
    print('Subtração = {}'.format(sub))
elif escolha == 'MUL':
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    mult = n1*n2
    print('Multiplicação = {}'.format(mult))
elif escolha == 'DIV':
    n1 = float(input('Digite o numerador: '))
    n2 = float(input('Digite o denominador: '))
    if n2 == 0:
        print('Erro! O denominador não pode ser nulo.')
    else:
        div = n1/n2
        print('Divisão = {:.1f}'.format(div))
else:
    print('Opção inválida!')
