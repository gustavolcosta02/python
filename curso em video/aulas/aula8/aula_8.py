from math import sqrt,ceil  #importa uma bibilhoteca no caso a de matematica/math ( se usar um from na frente vc pode expecificar o que importar da bibilhoteca requisitada )

num = int(input('Digite um numero: '))
raiz = sqrt(num)    #sqrt é a funcao de raiz 
print('a raiz de {} e igual a {}' .format(num, ceil(raiz)))  #aqui estou mostrando a raiz de uma forma aredondada pra cima a math.floor arredonda pra baixo 


