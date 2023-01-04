from random import randint, choice
print('Sorteio de um entre cinco alunos\n')
a1 = str(input('Insira o nome do primeiro aluno: '))
a2 = str(input('Insira o nome do segundo aluno: '))
a3 = str(input('Insira o nome do terceiro aluno: '))
a4 = str(input('Insira o nome do quarto aluno: '))
a5 = str(input('Insira o nome do quinto aluno: '))
lista = [a1, a2, a3, a4, a5]
#nome = lista[randint(0,4)] # método alternativo ao choice
nome = choice(lista)
print('\nO aluno escolhido foi {}.'.format(nome))
