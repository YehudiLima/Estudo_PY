""" try:
    internet = None
    print('Estabelecendo conexão com a ' + internet)
except TypeError as erro_internet:
    print("Nao a conexão com a internet!")
finally:
    print('Desfazendo as compras do carrinho!') """

try:
    valor = int(input('Digite um numero:',))
    print(valor / 0)
except ZeroDivisionError as erro_zero:
    print('Nao é possível dividir por zero!')
except ValueError as erro_int:
    print('Favor digitar apenas numeros')
finally:
    print('Operação cancelada, tente novamente')
