from random import sample
n1 = input('Nome do 1º aluno: ')
n2 = input('Nome do 2º aluno: ')
n3 = input('Nome do 3º aluno: ')
n4 = input('Nome do 4º aluno: ')
os = [n1, n2, n3, n4]
print('A ordem sorteada ficou decidida em {}!'.format(sample(os,4)))
