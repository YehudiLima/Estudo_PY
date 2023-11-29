tupla = (4, 2, 3.6)
print(tupla[0])
print(len(tupla))
print(type(tupla))
# Tuplas, funcionam com ou sem parenteses '()', é opcional.
# A funçao len verifica quantos itens tem a variavel.
# tuplas nao podem ser modificadas ou alteradas.

pessoa = ("Paulo", 67, True)
nome, idade, casado = pessoa
print(
    f"Seu nome é {nome}, \n voce tem {idade} anos, e \n voce é casado? {casado}")
