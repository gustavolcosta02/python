from datetime import date 

ano = int(input('Qual o ano do seu nascimento: '))
atual = date.today().year
idade = atual - ano

if idade <= 9:
    print('Você e um atleata Mirim')
elif idade >9 and idade <= 14:
    print('Você e um atleata Ifantil')
elif idade >14 and idade <=19:
    print('Você e um atleata Junior')
elif idade >14 and idade <=25:
    print('Você e um atleata Sênior')
else:
    print('Você e um atleata Master')