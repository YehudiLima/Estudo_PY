try:
    idade = int(input("Qual a sua idade?",))
    print(f'Sua idade é {idade}')

except:
    print('Favor, digite apenas numeros.')


# Especificando o erro com try and except
try:
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(numeros[15])

except IndexError as erro_indice:
    print('Favor, digitar um índice válido.')
    print(f'Mensagem de erro: {erro_indice}')
