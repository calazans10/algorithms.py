# -*- coding: utf-8 -*-


def func(x):
    print('x é', x)
    x = 2
    print('Variável local x mudou para', x)

x = 50
func(x)
print('x continua', x)
