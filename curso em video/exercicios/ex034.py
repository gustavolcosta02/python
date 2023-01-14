salario = float(input('Digite o valor do seu salario: '))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
  novo = salario + (salario * 10 / 100)

print('seu salario com aumento e: {}' .format(novo))
