"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 28
   Programador: Fernando Martins Cardoso
"""

print('###'*11)
print('#      Médias de 3 números      #'.upper())
print('###'*11)

print('''\nEste programa permite calcular a média de
três números de acordo com as seguintes opções:
1 - Média geométrica
2 - Média ponderada (pesos 1, 2 e 3)
3 - Média harmônica
4 - Média aritmética''')

escolha = int(input('Escolha qual tipo de média deseja calcular (1 a 4): '))

n1 = float(input('Insira o primeiro número: '))
n2 = float(input('Insira o segundo número: '))
n3 = float(input('Insira o terceiro número: '))

if escolha == 1:
    mg = (n1*n2*n3)**(1/3)
    print('Média geométrica de {}, {} e {} é igual a {:.2f}'.format(n1, n2, n3, mg))
elif escolha == 2:
    mp = (n1 + 2*n2 + 3*n3)/6
    print('Média ponderada de {}, {} e {} é igual a {:.2f}'.format(n1, n2, n3, mp))
elif escolha == 3:
    mh = 1/((1/n1) + (1/n2) + (1/n3))
    print('Média harmônica de {}, {} e {} é igual a {:.2f}'.format(n1, n2, n3, mh))
elif escolha == 4:
    ma = (n1 + n2 + n3)/3
    print('Média aritmética de {}, {} e {} é igual a {:.2f}'.format(n1, n2, n3, ma))
else:
    print('Erro! A escolha do tipo de média é inválida!')
    


