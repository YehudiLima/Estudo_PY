# Enumerate
""" for indice, numero in enumerate(range(1, 11), 0):
    print(indice, numero)
    if indice == 4:
        print("Estamos na metade da lista") """


""" nomes = ['nome1', 'nome2', 'nome3', 'nome4', 'nome5']

for indice, nome in enumerate(nomes, 0):
    print(indice, nome)
    if indice == 3:
        print('Ja temos 3 pessoas registradas')
 """

# Desafio 1

frutas = ['Maça', 'Laranja', 'Morango', 'Limão']

for indice, fruta in enumerate(frutas, 0):
    if indice == 3:
        print(f'{indice} {fruta} Em promoção')
    else:
        print(indice, fruta)
