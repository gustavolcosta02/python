n1 = float(input('Digite o valor da sua primeira nota: '))
n2 = float(input('Digite o valor da sua segunda nota: '))

media = (n1 + n2 ) /2

if media < 5:
    print('Você foi reprovado, sua media foi {}'.format(media))
elif media >=5 and media <6.9:
    print('Você esta de recuperação, sua media foi {}'.format(media))
elif media >= 7:
    print('Você foi aprovado com uma media de {}' .format(media))
