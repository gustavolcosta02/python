nome = str(input('Qual e seu nome? ')).strip()

if  nome == 'gustavo':
    print('Que nome lindo {} '.format(nome))
elif nome =='pedro' or nome =='maria':   #elif e o acrecimo de uma vertente de condicao para o if (else if)
    print('seu nome e bem popular no Brasil')   
elif nome in(' claudia ana  flavia'):
    print('Que belo nome feminino')
else:
    print('seu nome e bem normal {}' .format(nome))