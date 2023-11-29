# Trabalhando com Multipas listas
from itertools import zip_longest

""" a_lista = ['A', 'B', 'C', 'D', 'E']
b_lista = [1, 2, 3, 4, 6]

for a, b in zip(a_lista, b_lista):
    print(a)
    print(b) """

""" produto = ['produto 1', 'produto 2', 'produto 3', 'produto 4', 'produto 5']
preco = [250, 150, 100, 80, 200]

for a, b in zip(produto, preco):
    print(f'Este item {a} esta no valor de: R${b}') """

""" alunos = ['Carla', 'Matheus', 'Benaia', 'Joaquim']
notas = [7, 6, 8]
for aluno, nota in zip_longest(alunos, notas):
    print(f'O estudante(a) {aluno} teve uma nota de: {nota}') """

produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
precos = ['R$500,00', 'R$1.500,00', 'R$2.700,00', 'R$5.000,00']

for produto, preco in zip_longest(produtos, precos):
    print(f'Produto: {produto} encontrado no valor de: {preco}')
