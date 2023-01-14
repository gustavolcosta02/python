n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1<n2:
    print('o valor {} e amior que {}'.format(n2,n1))
elif n1>n2:
    print('o valor de {} e maior q {}'.format(n1,n1))
else:
    print('os valores sao iguais')
