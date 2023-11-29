""" 1. Escreva uma função que recebe um número inteiro positivo e retorna True caso ele
seja primo e False , caso contrário.
Sugestão:
def e_primo(n):
# Sua implementação aqui
print(e_primo(1))
# False
print(e_primo(2))
# True """


""" def e_primo(numero):
    if numero <= 1:
        return False  # 0 e 1 não são considerados primos
    if numero <= 3:
        return True  # 2 e 3 são primos

    if numero % 2 == 0 or numero % 3 == 0:
        return False

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6

    return True


numero = int(input("Digite um número natural positivo: "))

resultado = e_primo(numero)
print(resultado)
 """

""" 2. Implemente uma função que recebe uma lista de números inteiros e retorna uma
tupla (pos, num) , onde pos é a posição (ou índice) do maior número na lista e num
é o valor desse número. """


while True:

    usuario = int(input("Digite um numero inteiro ou digite [0] para sair:",))
    notas = []

    if usuario == 0:
        print("Sessao finalizada")
        break

    notas = usuario

else:
    print("Digite novamente ou [0] para sair:")

    print(notas)
