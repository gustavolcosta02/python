km = int(input('QUal e a velocidade do seu carro: '))



if km <= 80:
    print(('vc esta dentro do limite, tenha uma boa viagem'))
else:
    multa = (km-80)*7
    print('MULTADO! vc exedeu o limite permitido de 80KM vc deve pagar uma multa de R${:.2f}'.format(multa))