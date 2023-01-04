"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 21 - Versão modificada da questão 18
   Programador: Fernando Martins Cardoso
"""

print('###'*18)
print('#               Calculadora básica                   #'.upper())
print('#      Resolve as quatro operações fundamentais      #')
print('###'*18)

print('''Escolha a opção:
1- Soma de 2 números.
2- Diferença entre 2 números (maior pelo menor).
3- Produto entre 2 números.
4- Divisão entre 2 números (o denominador não pode ser zero). ''')
escolha = int(input('Opção: '))

if escolha == 1:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    soma = n1 + n2
    print('Soma = {}'.format(soma))
elif escolha == 2:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    if n1>n2:
        sub = n1 - n2
    else:
        sub = n2 - n1
    print('Diferença = {}'.format(sub))
elif escolha == 3:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    mult = n1*n2
    print('Produto = {}'.format(mult))
elif escolha == 4:
    n1 = float(input('Digite o numerador: '))
    n2 = float(input('Digite o denominador: '))
    if n2 == 0:
        print('Erro! O denominador não pode ser nulo.')
    else:
        div = n1/n2
        print('Divisão = {:.1f}'.format(div))
else:
    print('Opção inválida!')
