frase = str(input('digite uma frase: ')).strip().upper()

print('A letra A apareceu: {}'.format(frase.count('A')))
print('A primeira letra A apareceu na posicao: {}'.format(frase.find('A')+1))
print('A ultima letra a apareceu na posicao: {}'.format(frase.rfind('A')+1))