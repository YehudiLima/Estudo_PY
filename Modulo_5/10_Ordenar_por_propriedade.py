# Ordenar por propriedade 'itemgetter'

""" nomes = ['Zack', 'Roberto', 'Arthur', 'Mario']
valores = [21, 3, 56, 7, 2, 45, 12, 90, 76, 43, 23, 11, 6]

nomes.sort(reverse=True)
valores.sort(reverse=True)

print(nomes)
print(valores)
 """

# Desafio 1
from operator import itemgetter
""" 
produtos = [
    {"nome": "Celular",
     "preco": 1500
     },
    {"nome": "Monitor",
     "preco": 500
     },
    {"nome": "Microfone",
     "preco": 300
     }
]

produtos.sort(key=itemgetter("preco"))
print(produtos) """

# Desafio 2

""" equipamento_filmagem = [
    ("Tripé", 300),
    ("Câmera", 1700),
    ("Iluminação", 200),
]

equipamento_filmagem.sort(key=itemgetter(1), reverse=True)
print(equipamento_filmagem)
 """

# Desafio 3

cotacao_moedas = [["usd", 5.25], ["brl", 1.56], ["eur", 6.47]]

cotacao_moedas.sort(key=itemgetter(1))
print(cotacao_moedas)
