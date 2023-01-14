n_convercao = int(input('Digite o numero que Quer converter: '))

n_escolha  = int(input('Você quer converter para:\n binario [1] \n octal [2] \n exadecimal [3] '))

if n_escolha == 1:
    print('{} convertido pra binario: {} '.format(n_convercao, bin(n_convercao)[2:]))
elif n_escolha == 2:
    print('{} convertido pra octal: {} '.format(n_convercao, oct(n_convercao)[2:]))
elif n_escolha == 3:
    print('{} convertido pra exadecimal: {} '.format(n_convercao, hex(n_convercao)[2:]))
else:
    print('Por favor digite um numero entre 1, 2 e 3')