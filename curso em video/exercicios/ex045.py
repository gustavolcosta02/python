from codecs import raw_unicode_escape_encode
from random import randint

itens = ('pedra','papel','tesoura')
computador = randint(0,2)


escolha = int(input('escolha entre\n pedra[1]\n papel[2]\n tisoura[3]\n'))


print('o Computador escolheu {}'.format (itens[computador]))

if computador == 0 :        #pedra
    if  escolha == 1:
        print('Empate')
    elif escolha ==2:
        print('Voce ganhou papel ganha de pedra ')
    elif escolha == 3:
        print('Voce perdeu pedra ganha de tesoura')
    else:
        print('escolha um numero legitimo')    
elif computador ==1: 
     if  escolha == 1:
        print('voce perdeu papel ganha de pedra')
     elif escolha == 2:
        print('empate')
     elif escolha == 3:
        print('voce ganhou tesoura ganha de papel')
     else:
        print('escolha um numero legitimo')


elif computador == 2: 
    if  escolha == 1:
        print('voce ganhou pedra ganha de tesoura')
    elif escolha == 2:
        print('voce perdeu tesoura ganha de papel')
    elif escolha == 3:
        print('empate')
    else:
        print('escolha um numero legitimo')