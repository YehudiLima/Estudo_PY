usuarios = {"Alice", "Marcos", "Natan"}
usuarios_2 = set(["Alice", "Marcos", "Natan"])

""" print(usuarios == usuarios_2) """
# Nos Conjuntos podemos fazer com chaves '{}' ou com set([]).
# Nos Conjuntos nao pode ter elementos repetidos como ex.: {2 ,2, 4} à saída será 2, 4 no terinal.

usuarios.add("Bob")
print(usuarios)
# A funçao add() adiciona um elemento dentro do Conjunto e nao garantem a ordenaçao de elementos detro do Conjunto.

""" usuario_novo = usuarios | usuarios_2
print(usuario_novo) """

""" usuario_novo = usuarios - usuarios_2
print(usuario_novo) """

usuario_novo = usuarios & usuarios_2
print(usuario_novo)
