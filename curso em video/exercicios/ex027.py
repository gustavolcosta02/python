n = str(input('Digite seu nome compelto: ')).strip().upper()

nome = n.split()

print('o seu primeiro nome e: {}'.format(nome[0]))
print('o seu primeiro nome e: {}'.format(nome[len(nome)-1]))
