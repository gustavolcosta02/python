frase = str(input('frase: ')).strip().upper()

palavras = frase.split()
juntos = '' .join(palavras)
inverso = ''
for letra in range(len(juntos) -1 , -1,-1):
    inverso += juntos[letra]
print(juntos,  inverso)