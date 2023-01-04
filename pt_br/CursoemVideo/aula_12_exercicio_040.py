print('{:-^40}'.format('Cálculo da Média de Duas Notas'))

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota:'))
media = (n1+n2)/2
print('Tirando {} e {}, a média do aluno é {:.1f}.'.format(n1, n2, media))
if media < 5:
    print('O aluno está REPROVADO.')
elif media < 7:
    print('O aluno está de RECUPERAÇÃO.')
else:
    print('O aluno está APROVADO.')
