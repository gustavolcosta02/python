from random import randint

num = randint(0,5)

print('Vou pensar em um numero entre 0 e 5, tente acertar')
valor = int(input('digite seu valor: '))

if num == valor:
    print('parabens vc acertou, eu pensei no {} e vc escreveu {}'.format(num,valor))
else:
    print('GANHEI! eu pensei em {} e vc em {}'. format(num,valor))

