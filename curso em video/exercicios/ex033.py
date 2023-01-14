n1 = int(input('digite o primeiro valor '))
n2 = int(input('digite o segundo valor '))
n3 = int(input('digite o terceiro valor '))

menor = n1

if n2>n1 and n2>n3:
    menor = n2
if n3>n1 and n3>n2:
    menor = n3

maior = n1

if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

print('o seu maior valor e {} e seu menor valor e {}' .format(maior,menor))