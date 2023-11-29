""" def exibir_preço(nome_produto, preco):
    print(f'{nome_produto} esta no valor de: R${preco}')


# Argumentos Posicionais
exibir_preço("Leite Integral", 3.99)
# ou
#Argumentos Nomeados
exibir_preço(nome_produto="Arroz Integral", preco=6.99) """

# exercicio 1


def gerar_objeto_personalizado(cor, *, altura, formato):
    print("Sua cor é: ", cor)
    print("Sua altura é: ", altura)
    print("Seu formato é: ", formato)


gerar_objeto_personalizado("Branco", altura='22cm', formato='Triângulo')
