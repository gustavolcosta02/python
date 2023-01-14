print('{:=^40}'.format(' LOJAS 02 '))
preco = float(input('valor a ser pago: '))
desconto = int
forma_pagamento = int(input('Avita no Dinheiro[1]\nAvista no cheque[2]\ncartao[3]\n'))

if forma_pagamento == 1 or forma_pagamento ==2:
      preco = preco - (preco*10/100)
      print('o valor do seu produto e: {:.2f}'.format(preco))
elif forma_pagamento ==3:
    fatura_cartao = int(input('Quantas vezes você quer dividir no cartao\navista no cartao[1]\n2x no cartao[2]\n3x no cartao[3]\nDigite o numero de parcelas q vc deseja\n'))
else:
    print('escolha uma das poções validas')

if fatura_cartao == 1:
    preco = preco - (preco*5/100)
    print('o valor do seu produto e: {:.2f}'.format(preco))
elif fatura_cartao == 2:
    preco = preco/2
    print('Você vai pagar {} parcelas de R${:.2f}'.format(fatura_cartao,preco))
elif fatura_cartao ==3:
    preco = (preco + (preco*20/100)/3)
    print('Você vai pagar {} parcelas de R${:.2f}'.format(fatura_cartao,preco))
else :
    preco = (preco + (preco*20/100)/fatura_cartao)
    print('Você vai pagar {} parcelas de R${:.2f}'.format(fatura_cartao,preco))

