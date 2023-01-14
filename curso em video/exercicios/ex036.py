val_casa = float(input('Qual e o valor da casa? '))
val_sal = float(input('qual o valor do seu salrio? '))
ano = int(input('Em quantos anos vc quer financiar '))
prestacao = val_casa/(ano * 12)
minimo =   val_sal*30/100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestacao sera de {}'.format(val_casa,ano,prestacao))

if prestacao <= minimo:
    print('Seu imprestimo foi aceito')
else:
    print('Seu imprestimo foi negado')

