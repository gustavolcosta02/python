from math import radians, sin, cos, tan
angulo = float(input('Digite o valor de um angulo'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O angulo de {:.2f}\n tem o seno de {:.2f}\n o cosseno de {:.2f}\n e a tangente de {:.2f}' .format(angulo, seno, cosseno, tangente))

