"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 42
   Programador: Fernando Martins Cardoso
"""
print('###'*22)
print('#        Quadrado, cubo e raiz quadrada de um número real        #'.upper())
print('#        Inserir 0 ou número negativo, encerra o programa        #')
print('###'*22)

while True:
    n = float(input('Inserir número: '))
    if n <= 0:
        print('\nFinalizado')
        break
    else:
        quad = n**2
        cub = n**3
        raiz = n**0.5
        print('Quadrado de {} = {:.1f}'.format(n, quad))
        print('Cubo de {} = {:.1f}'.format(n, cub))
        print('Raiz quadrada de {} = {:.1f}'.format(n, raiz))
        print('============================')