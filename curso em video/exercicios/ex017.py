from math import hypot

cat_oposto = float(input('Digite o valor do cateto oposto do triangulo: '))
cat_adjacente = float(input('Digite o valro do cateto adjacente do triangulo: '))

hipotenusa = hypot(cat_oposto, cat_adjacente) 

print('A hipotenusa e {:.2f} ' .format(hipotenusa))