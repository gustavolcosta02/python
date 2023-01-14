km = float(input('Qantidade de km rodados: '))
dia = int(input('Quantos dia de aluguel: '))

valor_dia = dia *60
valor_km = km *0.15

total = valor_dia + valor_km

print('Você andou: {}kms, durante: {} dias danndo um valor de:{:.2f} aluguel' .format(km, dia, total,))