print('Cálculo de aumento no salário de um funcionário\n')
sal_atual = float(input('Digite o salário atual: R$'))
aumento_perc = float(input('Digite o aumento percentual (%): '))
novo_sal = sal_atual + aumento_perc*sal_atual/100
print('O funcionário que recebe R${:.2f}, com um aumento de {}%, passa a receber R${:.2f}.'.format(sal_atual, aumento_perc, novo_sal))
