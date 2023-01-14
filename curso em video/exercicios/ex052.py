n = int(input('valor: '))
tot = 0
for c in range(1, n + 1 ):
    if n % c ==0:
        print('\033[34m')
        tot +=1 
    else:
        print('\033[33m')
    print(c)
print ('o numero {} foi divisivel {} vezes'.format(n, tot))
if tot == 2:
    print('e por isso ele e primo')
else:
    print('e por isso ele n e primo ') 