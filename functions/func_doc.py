# -*- coding: utf-8 -*-


def printMax(x, y):
    """Imprime o maior entre dos números.

    Os dois valores devem ser inteiros."""

    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'é o maior')
    else:
        print(y, 'é o maior')


printMax(3, 5)
print(printMax.__doc__)
