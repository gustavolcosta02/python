r1 = float(input('digite o primeiro valor '))
r2 = float(input('digite o segundo valor '))
r3 = float(input('digite o terceiro valor '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segumentos a cima formao um triangulo ', end='')
    if r1 == r2 == r3:
        print('Equilatero')
    elif r1 != r2 != r3 !=r1:
        print('Escaleno')
    else:
        print('Isosceles')
    
else:
    print('os seguimentos a cima n formao um triangulo ')