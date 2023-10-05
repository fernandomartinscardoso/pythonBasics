"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 39
   Programador: Fernando Martins Cardoso
"""

print('###'*13)
print('#      Bônus adicional de salário     #'.upper())
print('###'*13)

salario_atual = float(input('Digite o salário atual: \nR$ '))

tempo_trab_anos = int(input('Digite quantos anos de trabalho na empresa: \n'))

if salario_atual <= 500:
    salario_novo = 1.25*salario_atual
elif salario_atual > 500 and salario_atual <= 1000:
    salario_novo = 1.20*salario_atual
elif salario_atual > 1000 and salario_atual <= 1500:
    salario_novo = 1.15*salario_atual
elif salario_atual > 1500 and salario_atual <= 2000:
    salario_novo = 1.10*salario_atual
else:
    salario_novo = salario_atual

if tempo_trab_anos < 1:
    salario_novo = salario_novo
elif tempo_trab_anos >= 1 and tempo_trab_anos < 4:
    salario_novo = salario_novo + 100
elif tempo_trab_anos >= 4 and tempo_trab_anos < 7:
    salario_novo = salario_novo + 200   
elif tempo_trab_anos >= 7 and tempo_trab_anos < 11:
    salario_novo = salario_novo + 300
else:
    salario_novo = salario_novo + 500

print('Para quem recebe um salário atual de R$ {:.2f} e tem {:d} ano(s) de trabalho na empresa, vai passar a receber R$ {:.2f}'.format(salario_atual, tempo_trab_anos, salario_novo))
