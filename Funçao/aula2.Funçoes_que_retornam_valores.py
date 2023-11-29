""" def calcular_conta(consumo, taxa_serviço, desconto_fidelidade):

    servico = consumo * taxa_serviço
    desconto = consumo * desconto_fidelidade
    valor = consumo + servico
    valor = valor - desconto
    return valor


valor = calcular_conta(consumo=200, taxa_serviço=0.5, desconto_fidelidade=0.1)
print(f"O valor a ser pago é: {valor}")
# Regra de Negócios """


"""
consumo = 100
serviço = consumo * taxa_serviço #10
desconto = consumo * desconto_fidelidade #5

valor = consumo + serviço # 110
desconto = valor - desconto # 110 - 5

=> 105

"""


""" def calcular_conta(consumo, taxa_serviço, desconto_fidelidade):

    if taxa_serviço == 0 and desconto_fidelidade == 0:
        return consumo

    """ """ servico = consumo * taxa_serviço
    desconto = consumo * desconto_fidelidade
    valor = consumo + servico
    valor = valor - desconto """
"""

print(F'O valor a ser pago é: {calcular_conta(100, 0, 0.0)}')
 """


def calcular_media_mediana(notas):
    resultado = sum(notas) / len(notas)

    return resultado


media = calcular_media_mediana([5, 5, 10])
print(media)
