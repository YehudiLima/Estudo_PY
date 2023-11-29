# While-Loop

""" while True:
    print("1")
    print("2") """

# While

""" a = 1

while a <= 100:
    print(a)
    a += 1
print("Fim") """

""" total = 0
while True:
    valor = float(input("Valor das compras:",))
    total = total + valor

    continuar = input("Deseja continuar [y/n]?")
    if continuar != "y":
        break
print("Seu valor total é:", total)
 """

total = 0
continuar = "y"

while continuar == "y":
    valor = float(input("Valor da compra:\n"),)
    total += valor

    continuar = input("Deseja continuar, [y/n]",)

print("Seu total é:", total)
