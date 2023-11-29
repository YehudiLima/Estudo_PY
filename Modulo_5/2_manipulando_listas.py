valores = [1, 2, 3, 4, 5, 1, 6, 7, 8, 9, 10]
anos = [2020, 2030, 2040, 2050]

# Adicionar ao final da lista 'append'
""" valores.append(11)
print(valores) """

# Unir listas 'extend'
""" valores.extend(anos)
print(valores) """

# Adicionar lista '+'
""" nova_lista = valores + anos
print(nova_lista) """

# Inserir valores na lista 'insert'
""" anos.insert(3, 2041)
print(anos)
 """
# Extrair com base no indice 'pop'
""" ano_extraido = anos.pop(1)
print(anos)
print(ano_extraido) """

# Remover item da lista
""" ano_removido = anos.remove(2020)
del anos[0]
print(anos) """

# contando a ocorrencia de um valor 'count'
""" print(valores.count(1)) """

# Resetar 'clear'
valores.clear()
print(valores)
