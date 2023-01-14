# fatiamaneto ex: frase(2:2:2)  o primeiro 2 representa o numero da casa de onde vai comecar a variavel
#                               o segundo  2 representa o numedo da casa de onde ele vai terminar seno q ele vai ler uma a menos da casa desejada
#                               e o ultimo 2 representa o numero de casas q ele vai pular para ler o frase escrita

frase = "Curso em Video Python"
print(frase[1:15:2])

# Analise  "lan(fease)" le o numero de caracteres dentro de uma frase 
# ex "frase.count(e)" mostra quantos letras "e" tem na sua frase
# ex "frase.finde(deo)" ele encontra onde esta o termo escolhido indiacando a sua casa inicial 

print(len(frase.strip()))


#transformacao "frase.replace(Python, Android)" ele troca o termo escolhido da frase pelo outro 
# "frase.upper()" trnasforma tas as letras minusculas em maiusculas da frase
# "frase.lower()"  transforma todas as letras maiusculas em minusculas 
# "frase.capitalize()"  transforma apenas a primeria letra em maiuscula 
# "frase.title()"  ele transforma TODAS AS PRIMEIRAS LETRAS de uma frase em maisculo ex: Gustavo Leandro
# "frase.strip()" removo todoas os espaçoes extras na frase que ficao no comeco e no final 
# "frase.rstrip()" remoso somente os ultimos espaços da direita || o mesmo vale pro "fase.lstrip" q remove os espaços da esquerda 

print(frase.replace('Python', 'Androido'))
print(frase.upper().count('O'))

#Divisao "frase.split()"  ele pegas uma frase e a separa em palavras as recolocando em uma lista numerando elas comecando a partir de 0

dividido = frase.split()
print(dividido[0][3])  #a segunda chave ele pega a caracter de numero 3 da palavra 0 da lista

#juncao  "  '-'.join(frase) "  ele junta a as palavras divididas pelo split e coloca um - no lugar dos espaços

