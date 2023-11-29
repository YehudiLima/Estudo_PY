nome = input("Qual é o seu nome?:",)
idade = int(input("Qual é a sua idade?:",))
peso = float(input("Qual é o seu peso?:",))
altura = float(input("Qual a sua altura?:",))
estado_civil = input("Voce é casado, responda com [y/n]?",)


print("Seu nome é:", nome)
print("Sua idade é:", idade)
print("Seu peso é:", peso)
print("Sua altura é:", altura)

if estado_civil == "y":
    print("Seu estado civil é casado")
else:
    print("Seu estado civil NAO é casado")
