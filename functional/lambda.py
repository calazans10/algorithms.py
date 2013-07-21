# -*- coding: utf-8 -*-


def cria_repetidor(n):
    return lambda s: s * n

dobro = cria_repetidor(2)

print(dobro('palavra'))
print(dobro(5))
