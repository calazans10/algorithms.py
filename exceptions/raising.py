# -*- coding: utf-8 -*-


class ShortInputException(Exception):
    '''Uma classe exceção definida pelo usuário.'''

    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Entre com alguma coisa >>> ')

    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('Por que você jogou um EOF em mim?')
except ShortInputException as e:
    print('ShortInputException: A entrada teve o comprimento {0}, o \
esperado era pelo menos {1}'.format(e.length, e.atleast))
else:
    print('Nenhuma exceção foi levantada.')
