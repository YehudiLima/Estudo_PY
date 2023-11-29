# Conversao entre tipos

# Int
""" idade = int(input('Qual a sau idade?',))
print(idade >= 18) """

# Str
""" ano_publicacao = 2023
print(f'Este livro foi publicado no ano de {ano_publicacao}.')
print('Este livro foi publicado no ano de', ano_publicacao)
print('Este livro foi publicado no ano de ' + str(ano_publicacao)) """

# Float

""" altura = float(input('Qual a altura da parede?',))
print(altura > 2.50)
 """

# Conversoes entre coleçoes

saudaçoes = 'Hello!'

print(list(saudaçoes))
print(set(saudaçoes))
print((saudaçoes))
print(tuple(saudaçoes))
print(list(range(1, 31)))

numeros = [10, 20, 20, 40, 50]

print(set(numeros))
print(tuple(numeros))
