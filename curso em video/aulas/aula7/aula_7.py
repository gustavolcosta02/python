# o simbolo de % e o rsto de umaa divisao ( 5%2 == 1)
# o simbolo de // e a divisao inteira (5//2 == 2)

# orderm de precedencia aritimetica python 
#1- ()
#2- **
#3- * / // %
#4- + -
# um exemplo de raiz quadrada 81**(1/2)
#para tirar a % de um valor vc divide a % por 100 e multiplica pelo numero no qual vc quer a procentagem 

n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n1
e = n1 ** n2

print('A soma dos valor e: {},\n O produto e {}, E a divisao e {:.3f}' .format(s, m, d), end=' ,')  #o (:.3f) aredonda o numero para 3 casas decimais  || o end no final funciona para quebrar a linha de baixo e juntar os dois print numa so||  o \n quebra a linha adicionando o texto seguinte na linha a baixo
print('A divisao inteir: {}, É potencia:{} ' .format(di, e))

