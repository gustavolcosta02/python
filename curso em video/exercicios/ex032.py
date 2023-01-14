from datetime import date  #bibilhoteca de tempo e data 

ano = int(input('Que ano quer analisar? coloque 0 para o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0  or ano % 400 == 0:   #calculo para ano bissexto 
    print('o ano {} e bissexto'.format(ano))
else:
    print('o ano {} nao e bissexto'.format(ano))