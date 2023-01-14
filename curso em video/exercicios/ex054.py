from datetime import date
atual = date.today().year

velho = 0
novo = 0

for c in range(0,7):
    nasc = int(input('ano do seu nascimento: '))
    idade = atual-nasc
    if idade >=21:
        velho += 1
    else: 
        novo += 1
print('temos {} novos e {} velhos'.format(novo,velho))