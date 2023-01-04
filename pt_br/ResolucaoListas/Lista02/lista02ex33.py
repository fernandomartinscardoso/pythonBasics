"""Gabarito da Lista 2 - Comandos Condicionais
   Exercício 33
   Programador: Fernando Martins Cardoso
"""

print('###'*13)
print('#          Reajuste de Preço          #'.upper())
print('###'*13)

pr_ant = float(input('Digite o preço antigo: R$'))

if pr_ant >= 0 and pr_ant <= 50:
    pr_novo = 1.05*pr_ant
    print('Novo preço: R${:.2f}'.format(pr_novo))
    print('Reajuste de 5%')
elif pr_ant > 50 and pr_ant <= 100:
    pr_novo = 1.1*pr_ant
    print('Novo preço: R${:.2f}'.format(pr_novo))
    print('Reajuste de 10%')
elif pr_ant > 100:
    pr_novo = 1.15*pr_ant
    print('Novo preço: R${:.2f}'.format(pr_novo))
    print('Reajuste de 15%')
else:
    print('Preço inválido. Valor precisa ser positivo')

if pr_novo <= 80:
    print('Classificação do produto: Barato')
elif pr_novo > 80 and pr_novo <= 120:
    print('Classificação do produto: Normal')
elif pr_novo > 120 and pr_novo <= 200:
    print('Classificação do produto: Caro')
else:
    print('Classificação do produto: Muito Caro')
