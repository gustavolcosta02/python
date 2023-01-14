from locale import delocalize
from tkinter import CENTER


num = int(input('digite um valor: '))


unidade = num //1 % 10
dez = num //10 % 10
cen =  num //100 % 10
mil = num //1000 % 10

print('Analisando o numero {:.0f}\n o numero tem {:.0f} unidade\n tem {:.0f} dezena\n tem {:.0f} centena\n tem {:.0f} milhare'.format(num,unidade,dez,cen,mil))

#outra forma de fazer mas dessa vez transformando o numero em str

n= str(num)
print('analise do numero{}'.format(num))
print('unidade {}' .format(n[3]))
print('dezena {}'.format(n[2]))
print('centena {}'.format(n[1]))
print('milhar {}'.format(n[0]))


#os dois jeitos sao funcionais mas um trabala no os numero no valor int do incio ao fim o outro passa pra string para facilitar o calculo 