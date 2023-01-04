"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 38
   Programador: Fernando Martins Cardoso
"""

print('###'*23)
print('#      Busca do terno pitagórico cuja soma seja igual a 1000:       #'.upper())
print('#                      a²+b²=c² e a+b+c=1000                        #')
print('###'*23)

print('\nO terno pitagórico que atende ao enunciado é: ')

for a in range(1, 1000):
    for b in range(1, 1000):
        if a**2+b**2==(1000-a-b)**2:
            c = 1000-a-b
            print(a, b, c)
            