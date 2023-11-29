# Funçoes

""" def dar_boas_vindas():
    print("Bem-Vindo")


dar_boas_vindas() """


""" def boas_vindas(nome):
    print(f'Bem-Vindo(a) {nome}')


boas_vindas("Yehudi")
boas_vindas("Carlos") """

# Exercicio 1


""" def gerar_nome_completo(nome, sobrenome, evento):
    print(f"Seja bem-vindo(a) {nome} {sobrenome} ao {evento} ")


gerar_nome_completo(nome='Yehudi', sobrenome='Lima', evento='Jurassic Park')
 """
# Exercicio 2


def calcular_valores(produto_preço, quantidade=1):
    print(f'O valor do produto é R${produto_preço * quantidade}')


calcular_valores(produto_preço=12.34, quantidade=2)
