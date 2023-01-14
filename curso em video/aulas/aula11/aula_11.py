nome = 'gustavo'

cores = {'azul':'\033[34m','amarelo':'\033[33m'}

print('\033[1;30;43m hello world!\033[m')

print ('ola {}{}{}'.format('\033[0;34;40m', nome, '\033[m'))

print('ola{}{}'.format(cores['amarelo'], nome))