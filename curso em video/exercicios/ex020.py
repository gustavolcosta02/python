from random import  shuffle  #randomiza valores

n1 = input('primeiro aluno: ')
n2 = input('segundo aluno: ')
n3 = input('terceiro aluno: ')
n4 = input('quarto aluno: ')

lista = [n1, n2, n3, n4]

shuffle( lista )

print('A ordem dos alunos e: {}' .format(lista))

