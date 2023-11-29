# Criar lista com:
# Range
lista = list(range(0, 6))
print(lista)

# Map

nomes = ['John', 'Larissa', 'Gorge', 'Gustavo']


def aprovar_pessoas(nome):
    return nome + ' ' + 'APROVADO!'


print(list(map(aprovar_pessoas, nomes)))
