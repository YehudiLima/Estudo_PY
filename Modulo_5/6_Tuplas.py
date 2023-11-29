sites = ('instagram.com', 'facebook.com', 'youtube.com')
valores = (9.99, 7.99, 8.99)
print(sites[1])

# Injuntar tuplas com Zip
for site, valor in zip(sites, valores):
    print(f'O site {site} esta com assinatura de apenas {valor}')

# Uniao de tuplas

dados_do_pacote = sites + valores
print(dados_do_pacote)

# Acesso de valores em uma tupla
print(dados_do_pacote[2])
print(dados_do_pacote[5])
