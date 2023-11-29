# **Kwargs(Keyword agument)-Quantidade ilimitade de elementos Nomeados
""" def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)


concatenar(a="Nao", b="somos", c="fracos!")
 """


def fazer_calculo(nome, *args, **kwargs):
    print(nome)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for kwarg in kwargs.values():
        print(kwarg)


fazer_calculo("Jorge", 4, 5, 3, 2.6, 7, a=21, b=43, c="Ola")
