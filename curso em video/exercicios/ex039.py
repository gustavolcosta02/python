from datetime import date 
atual = date.today().year
nasc = int(input('Qual o ano do seu nascimento: '))
idade = atual - nasc
print(idade)
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade 
    print('você n tem 18 anos, ainda faltam {} para o alistamento'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado a {} anos'.format(saldo))
 