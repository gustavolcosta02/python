n = float(input('Qual a altura da sua parede'))
n2 = float(input('Qual a largura da sua parede'))


m4 = n*n2

tinta = m4/2

print('Sua parede tem{}x{} e sua area e {}.\n Para pintar a parede vc vai precisar de {}m² litros de tinta' .format(n, n2, m4, tinta))