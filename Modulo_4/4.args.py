def somar(*valores, b):
    print(valores)
    for valor in valores:
        b += valor
        print(b)


somar(15, 10, 5, b=20)
# *args
