soma = 0
contador = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        contador += 1 
        soma += c
        
print('a soma de  todos os {} valor e {}'.format(contador,soma))
    
