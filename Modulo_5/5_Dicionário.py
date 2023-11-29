# Dicionario {keys:values}
dicionario_pessoas = {'nome': 'Carlos', 'idade': 32, 'altura': 1.78}
print(dicionario_pessoas)
# ou
dicionario_pessoas2 = dict(nome="Roberto", idade=21, altura=1.87)
print(dicionario_pessoas2)
# ambas as formas estao corretas, escolha uma de sua preferencia
""" print(dicionario_pessoas['nome'])
print(dicionario_pessoas2['nome'])
print(dicionario_pessoas['idade'])
print(dicionario_pessoas2['idade'])
print(dicionario_pessoas['altura'])
print(dicionario_pessoas2['altura']) """

""" print(dicionario_pessoas.keys())
print(dicionario_pessoas.values())
print(dicionario_pessoas.items()) """

for item in dicionario_pessoas.items():
    print(item)
