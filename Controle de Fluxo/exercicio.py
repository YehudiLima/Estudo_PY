# 2

""" a = int(input("Digite o primeiro valor:",))
b = int(input("Digite o segundo valor:",))
operador = int(input(
    "Digite o operador desejado, 1 para +, 2 para -, 3 para *, 4 para / ou //, 5 para **, 6 para &:",))
final = a + operador + b

if operador == 1:
    final = a + b
    print("Resultado:\n", final)
elif operador == 2:
    final = a - b
    print("Resultado:\n", final)
elif operador == 3:
    final = a * b
    print("Resultado:\n", final)
elif operador == 4:
    final = a / b
    print("Resultado:\n", final)
elif operador == 5:
    final = a ** b
    print("Resultado:\n", final)
elif operador == 6:
    final = a & b
    print("Resultado:\n", final)
print("Fim da operaçao")
 """

# 3

""" usuario = "Callahan"
senha = "12345"

nome_usuario = input("Informe o nome do usuário:",)
informe_senha = input("Informe a senha:",)

if nome_usuario != usuario and senha != informe_senha:
    print("Nome de usuario e senha incorretos")
elif nome_usuario == usuario and informe_senha != senha:
    print("Senha incorreta")
elif nome_usuario != usuario and informe_senha == senha:
    print("Nome de usuário inválido")
else:
    print("Autenticaçao bem-sucedida") """

# 4 While

""" a = 1

while a <= 100:
    print(a)
    a += 1
print("Fim") """

""" a = 0

while a <= 100:
    print(a)
    a += 2
print("Fim") """

numero = 6

usuario = int(input("Digite o numero:"),)

#

for usuario in range(3):
    print("Numero errado")
    break

if usuario < numero:
    print("Valor abaixo")
elif usuario > numero:
    print("Valor acima")
else:
    print("Parabens")

print("Fim do jogo")
