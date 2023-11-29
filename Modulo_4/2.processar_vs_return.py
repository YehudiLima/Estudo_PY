# Processa

""" def exibir_cotaçao_do_dia(moeda):
    if moeda == "usd":
        print(5.47)


exibir_cotaçao_do_dia(moeda='usd') """

# Return- use quando vc quer usar aquele valor em outras informaçoes a frente.


def exibir_cotaçao_do_dia(moeda):
    if moeda == "usd":
        return 5.47


cotaçao = exibir_cotaçao_do_dia(moeda="usd")
if cotaçao > 5:
    print("Investir na bolsa de valores nos EUA")
else:
    print("Investir depois")
