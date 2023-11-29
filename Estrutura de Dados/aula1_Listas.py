""" notas = [5, 8, 4.5]
#        0  1   2
notas.append(32)
notas.append(54)
print(notas[3]) """
# Funçao append() adiciona ao final  da lista

""" notas = [4, 5, 2, 3, 1]
notas.sort()
print(notas) """
# Funçao sort() organiza a lista em ordem organizada crescente.

""" notas = [4, 5, 2, 3, 1]
notas.sort(reverse=True)
print(notas) """
# Funçao sort(reverse=True) organiza em ordem drecrescente.

""" notas = [4, 5, 2, 3, 1]
notas.pop()
print(notas)
o = notas.pop()
print("->", o) """
# Funçao pop() apaga o ultimo item de uma lista.

""" notas = [4, 5, 2, 3, 1]
notas.insert(5, 6)
print(notas) """
# Funçao insert() adiciona um item e permite adiciona-lo em qualquer porta.

""" notas = [4, 5, 2, 3, 1]
notas.pop(0)
print(notas) """
# Funçao pop("adicionar a porta da lista") permite apagar um iten na porta que vc escolheu.

""" pessoa = ["Gabriel", 32, "99872-3245", "72.3Kg", "065-432-778-21"]

print("Nome do indivíduo:", pessoa[0])
print("Idade do indivíduo:", pessoa[1])
print("Telefone do indivíduo:", pessoa[2])
print("Peso do indivíduo:", pessoa[3])
print("CPF do indivíduo:", pessoa[4]) """
# Tambem podemos armazenar vario tipos de itens na Lista como Strings, Int, Float e Bool.

""" pessoas = [
    ["Fabio", 21]
    ["Roberto", 30]
    ["Pedro", 35]
] """
# Podemo scolocar Listas dentro de Listas.

""" lista = [0, "String", 4.6, []]
# print(lista)
for elemento in lista:
    print(f"O elemento da lista é: {elemento}") """
# Usando o For em uma Lista.

""" pares = [2, 4, 6, 8]
impares = [1, 3, 5, 7] """

""" print(pares[2] * impares[1])
print(pares[2] ** impares[1])
print(pares[2] // impares[1])
print(pares[2] & impares[1])
print(f"O segundo elemento da variável \'pares\' é: {pares[1]}")
print(f"O segundo elemento da variável \'impares\' é: {impares[1]}")
 """
# Podemos fazer calculos nas 'listas'

""" print(pares[-1])
print(pares[-2])
print(pares[-3]) """
# Indexaçao negativa

alunos = ["Joao", "Ana", "Clara", "Jose", "Bento"]

""" print(alunos[0])
print(alunos[1])
print(alunos[2])
print(alunos[3])
print(alunos[4]) """

for aluno in alunos:
    print(f"O nome do aluno é: {aluno}")
