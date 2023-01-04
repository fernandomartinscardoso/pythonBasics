"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 14
   Programador: Fernando Martins Cardoso
"""

print('###'*17)
print('#      Média ponderada de 3 notas e aprovação     #'.upper())
print('#    Este programa trabalha com notas de 0 a 10   #')
print('###'*17)

print('''\nSistema de avaliação: 
Média de 0,0 a 2,9 - Reprovado
Média de 3,0 a 4,9 - Recuperação
Média de 5,0 a 10,0 - Aprovado''')

n1 = float(input('Insira a nota do Trabalho de Laboratório: '))
if n1<0 or n1>10:
    print('Nota do Trabalho de Laboratório inválida!')
    quit()
n2 = float(input('Insira a nota da Avaliação Semestral: '))
if n2<0 or n2>10:
    print('Nota da Avaliação Semestral inválida!')
    quit()
n3 = float(input('Insira a nota do Exame Final: '))
if n3<0 or n3>10:
    print('Nota do Exame Final inválida!')
    quit()
# mp é a média ponderada que equivale a soma das notas multiplicadas pelos pesos dividida pela soma dos pesos
mp = (n1*2 + n2*3 + n3*5)/10
print('Média = {:.1f}'.format(mp))
if mp < 3:
    print('Situação: Reprovado')
elif mp < 5:
    print('Situação: Recuperação')
else:
    print('Situação: Aprovado')





