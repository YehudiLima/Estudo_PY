# listas

""" preco = [10, 20, 30, 33, 45, 765, 234567, 87654, 3456, 76, 54,
         21, 14, 87, 50, 65, 321, 765, 123, 87789, 2123, 5321, 78875]
print(preco[1])  # Índice
print(len(preco))
print(preco[preco.index(87)])
print(preco[preco]) """
# Listas no python sao dinamicas(aceitam qualquer tipo de dados)

""" listas = []

codigo = input("Rg:",)
nota = float(input("Nota:",))
resultado = codigo, nota
listas.append(resultado)

print(listas) """

""" listas_de_dez = [10] * 10
listas_de_Olas = ["OLa"] * 10
print(listas_de_dez)
print(listas_de_Olas) """

""" faixa_de_numero = list(range(21))
print(faixa_de_numero)
 """

""" lista_lista = [["Marco", 23], ["Carlos", 32]]
print(lista_lista[1][0]) """

# Desafio 1

""" objetos_mais_usados = list(["Biblia", "Computador", "Carro"])
print(objetos_mais_usados) """

# Desafio 2

""" contador = list(range(10, 31))
print(contador) """

# Desafio 3

""" print(objetos_mais_usados, contador) """

# Desafio 4

objetos = [["Biblia", "Computador", "Carro"],
           ['R$:300.00', "R$:800.00", "R$:7.000.00"]]
print("______________")
print(objetos[0][0])
print(objetos[1][0])
print("______________")
print(objetos[0][1])
print(objetos[1][1])
print("______________")
print(objetos[0][2])
print(objetos[1][2])
print("______________")
