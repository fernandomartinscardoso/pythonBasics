from random import sample, shuffle
print('Sorteio da ordem de apresentação de cinco alunos\n')
a1 = str(input('Insira o nome do primeiro aluno: '))
a2 = str(input('Insira o nome do segundo aluno: '))
a3 = str(input('Insira o nome do terceiro aluno: '))
a4 = str(input('Insira o nome do quarto aluno: '))
a5 = str(input('Insira o nome do quinto aluno: '))
lista = [a1, a2, a3, a4, a5]
'''nome = sample(lista,5)
print('\nA ordem de apresentação dos alunos é: {}.'.format(nome))'''

#Método alternativo
shuffle(lista)
print('\nA ordem de apresentação dos alunos é: {}.'.format(lista))
