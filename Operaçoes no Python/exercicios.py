# 1 - Saber se o numero é par ou impar
""" numero = int(input("Digite qualquer valor numero:",))
resultado = numero % 2

if resultado == 0:
    print("É um numero par")
else:
    print("É um numero impar")
 """
# 2

""" a = 5
b = 10
x = True
y = False
print((x or y) and (a < b))
print((x or y) and not (a < b))
 """

# 3

""" resultado = 2 + 3 * 2 ** 2
print(resultado) """

""" resultado = 2 + (3 * 2) ** 2
print(resultado)
 """

""" resultado = 2 + (3 * 2 ** 2)
print(resultado) """

# 4

valor_de_compra = float(input("Valor da compra:"),)
valor_frete = float(input("Valor do frete:"),)
cadastrado_no_programa = input("Cadastrado no programa? Responda com [y/n]:",)

compra_frete = valor_de_compra + valor_frete

if compra_frete > 100 or cadastrado_no_programa == "y":
    print("O cupom pode ser utilizado")
else:
    print("O cupom NAO pode ser utilizado")
