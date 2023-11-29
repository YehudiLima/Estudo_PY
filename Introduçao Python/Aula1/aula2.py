# Strings = "Ola Mundo"
# Inteiro = 1,2,3,4,5...213,214...
# Float = 1.23, 7.54, 5.55, 2.435 ...
# Booleano = True, False

# Exercicio 1

# Funçao type
print(type("Ola Mundo"))
print(type(12))
print(type(12.5))
print(type(True))

# Exercicio 2

valor_compras = float(input("Quantidade total das compras: "))
desconto = float(input("Valor do desconto a ser aplicado: "))
quantidade_itens = int(input("Quantidade de itens: "))

valor_final = valor_compras - desconto
print("Valor total com o desconto: ", valor_final)

custo_medio = valor_final / quantidade_itens
print("Custo medio de cada produto: ", custo_medio)
