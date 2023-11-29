""" 1: Escreva um programa que lê números inteiros positivos do usuário, um após o
outro, e monta uma lista a partir desses números e depois imprime a lista montada.
O programa deve continuar solicitando por números até que o elemento digitado
seja um número negativo (que não deve ser inserido na lista).
 """


""" numero = []
while True:
    usuario = int(input(
        "Digite um numero positivo inteiro (ou digite um numero negativo para sair):"),)
    if usuario < 0:
        break
    print(f"Numero digitado foi: {usuario}")
    numero.append(usuario)

print(f'Elementos da lista:{numero}')
print("Programa finalizado.")
 """


""" 2-Dada uma lista de números inteiros, escreva um programa que calcula a soma de
todos os números na lista.
Se preferir, pode utilizar a lista abaixo como exemplo:
lista = [1, 10, 20, 35, 22, 12]
# Resultado deve ser = 100 """

""" lista = [1, 10, 20, 35, 22, 12]

print(
    f'A soma dos elementos é: {lista[0]} + {lista[1]} + {lista[2]} + {lista[3]} + {lista[4]} + {lista[5]}')
soma = lista[0] + lista[1] + lista[2] + lista[3] + lista[4] + lista[5]
print("O resultado é:", soma)
 """

""" lista = [1, 10, 20, 35, 22, 12]

for elemento in lista:
    resultado = lista[0] + lista[1] + lista[2] + lista[3] + lista[4] + lista[5]
print("O resultado é:", resultado)
 """


""" #3-Data uma lista de números inteiros, escreva um programa que calcula a média dos
números na lista. O resultado não deve incluir números decimais. Exemplo: 12.3
deve imprimir apenas 12 .
Se preferir, pode utilizar a lista abaixo como exemplo:
lista = [1, 10, 20, 35, 22, 12]
# Resultado deve ser 16 """

""" lista = [5, 5]
media = lista[0] + lista[1] // 6
print('A média é:', media) """


""" 4. Suponha o seguinte programa:
# Alunos e suas respectivas notas
alunos = [
("Alice", 8),
("Bob", 7),
("Carlos", 9),
]
Escreva uma programa que calcula a média das notas de todos os alunos.
 """

""" alunos = [
    ("Alice", 8),
    ("Bob", 7),
    ("Carlos", 9),
] """

""" media = alunos[0][1] + alunos[1][1] + alunos[2][1]

print("Alice: \n")
print(alunos[0][1])
print("Bob: \n")
print(alunos[1][1])
print("Carlos: \n")
print(alunos[2][1])

print(f'Media das notas dos alunos: {media}')
 """


""" 5. Suponha o seguinte programa:
Exercícios – Estruturas de dados 2
# Alunos e suas notas representados através de dicionários
alunos = [
{
"nome": "Alice",
"nota": 8,
},
{
"nome": "Bob",
"nota": 7,
},
{
"nome": "Carlos",
"nota": 9,
}
]
Escreva uma programa que calcula a média das notas de todos os alunos. """

""" alunos = [
    {
        "nome": "Alice",
        "nota": 8,
    },
    {
        "nome": "Bob",
        "nota": 7,
    },
    {
        "nome": "Carlos",
        "nota": 9,
    }
]

media = alunos[0]["nota"] + alunos[1]["nota"] + alunos[2]["nota"]

print("Alice: ", alunos[0]["nota"])
print("Bob: ", alunos[1]["nota"])
print("Carlos: ", alunos[2]["nota"])

print(f'A média das notas dos alunos é: {media}')

 """

""" 6. DESAFIO. Escreva um programa que dado uma lista de números inteiros, imprime
o maior número dessa lista.
lista = [1, 3, 2, 5]
...
# Deve imprimir 5 """

""" lista = [1, 3, 2, 5]

maior_numero = max(lista)
menor_numero = min(lista)
print('O maior numero da lista é:', maior_numero)
print('O menor numero da lista é:', menor_numero) """


""" 7. DESAFIO. Uma string ( str ) também pode ser percorrida utilizando o for .
for x in "abc":
print(x)
# Vai imprimir:
# a
# b
# c
Escreva um programa que solicite uma string para o usuário e imprima quantas
vezes cada letra aparece na palavra. Por exemplo:
"banana"
# O resultado deve ser
{
'a': 3,
'b': 1,
Exercícios – Estruturas de dados 3
'n': 2
} """


