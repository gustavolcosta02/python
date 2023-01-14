nome = str(input('digite seu nome completo: ')).strip()

dividido = nome.split()

print('O seu nome em maiusculo e:{} '.format(nome.upper()))
print('O seu nome em minusculo e:{} '.format(nome.lower()))
print('seu nome tem {} caracteres'.format(len(nome)-nome.count(' ')))
print('seu primeiro nome e: {}' .format(dividido[0]))
print('seu primeiro nome tem: {} letras'.format(nome.find(' ')))   #nome.finde vai contar de 0 ao primeiro espaco, assim me contando quantas caracteres tem o primeiro nome