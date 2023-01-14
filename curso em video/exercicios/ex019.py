from random import choice

num1 = input('Nome do primero aluno: ')
num2 = input('Nome do segundo aluno?: ')
num3 = input('Nome do terceiro aluno: ')
num4 = input('Nome do quarto aluno: ')

lista = [num1, num2, num3, num4]    #criacao de lista no py
sorteio = choice(lista)

print('O aluno sortiado foi {}' .format(sorteio))

