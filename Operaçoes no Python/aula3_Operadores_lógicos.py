# Operadores Logicos
# not
# and
# or

# not

""" idade = 21
maior_idade = idade > 18
menor_idade = not maior_idade

print("Sua idade é:", idade)
print("É maior de idade:", maior_idade)
print("É menor de idade:", menor_idade) """

# and
""" 
usuario_correto = True
senha_correta = False
sucesso = usuario_correto and senha_correta
print("Login efetuado com sucesso?:", sucesso) """

# or

identidade = False
habilitaçao = False
dispensado = identidade or habilitaçao

if identidade == True or habilitaçao == True:
    print("Voce esta liberado")
else:
    print("Compareça a delegacia mais proxima")
