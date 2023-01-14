primeiro = int(input('Digite o primeiro valor '))
razao = int(input('razao: '))
decimo = primeiro + (10-1)* razao
for c in range (primeiro, decimo+razao, razao ): 
    print(c)