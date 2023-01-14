txt = input('Digite algo: ')

print('O tipo do seu texto e' ,type(txt))
print('So tem espaços?', txt.isspace())  #espaços
print('E um numero?', txt.isnumeric ())  #apenas numeros
print('E alfabetico?', txt.isalpha())   #apenas texto
print('E alphanumerico?', txt.isalnum())   #texto e numeros
print('Esta em maiusculas?', txt.isupper())  #letras maiusculas
print('Esta em minusculas?', txt.islower())  #letras minusculas
print('Esta captalizada?', txt.istitle())   #primeira letra maiuscula