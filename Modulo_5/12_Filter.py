""" # filter
nomes = ['John', 'Larissa', 'Goerge', 'Gustavo']


def pessoa_aprovada(pessoa):
    if pessoa == "Goerge":
        return True
    else:
        return False


print(list(filter(pessoa_aprovada, nomes)))
print(list(map(pessoa_aprovada, nomes)))
 """

# Desafio 1

vagas = [
    ['vaga 1', 1200],
    ['vaga 2', 2550],
    ['vaga 3', 5000]

]


def salario_mais_2500(salario):
    if salario[1] > 2500:
        return True
    else:
        return False


print(list(filter(salario_mais_2500, vagas)))
print(list(map(salario_mais_2500, vagas)))
