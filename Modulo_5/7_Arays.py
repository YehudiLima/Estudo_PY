# Arrays
from array import array
# Inteiro, Decimais e Caracteres

numeros = array("i", [1, 2, 3, 4, 5, 6])
print(numeros)
numeros.append(7)
print(numeros)
numeros.pop(3)
print(numeros)
numeros.insert(2, 33)
print(numeros)
numeros.remove(1)
print(numeros)
del numeros[3]
print(numeros)
