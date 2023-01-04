"""Gabarito da Lista 3 - Comandos de Repetição
   Exercício 43
   Programador: Fernando Martins Cardoso
"""
print('###'*22)
print('#             Idade média de um grupo de indivíduos              #'.upper())
print('#             Inserir o número 0 encerra o programa              #')
print('###'*22)

s = 0
c = 1
while True:
    idade = int(input('Insira a {}ª idade ou 0 para sair: '.format(c)))
    if idade == 0:
        break
    s = s + idade
    c = c + 1      
    
media = s/(c-1)
print('\nA média das {} idades inseridas é igual a: {:.1f}'.format((c-1), media))