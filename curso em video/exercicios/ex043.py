altura = float(input('Qual sua altura '))
peso = float(input('Qual o seu peso'))
imc = peso /(altura ** 2)

if imc <18.5:
    print('Você esta abaixo do peso')
elif imc >18.5 and imc <25:
    print('pesso ideal')
elif imc >25 and imc <30:
    print('sobrepeso')
elif imc >30 and imc < 40:
    print('obesidade')
else:
    print('obeidade morbida')