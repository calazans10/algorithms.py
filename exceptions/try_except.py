# -*- coding: utf-8 -*-


try:
    texto = input('Entre com alguma coisa >>> ')
except EOFError:
    print('Por que você jogou um EOF em mim?')
except KeyboardInterrupt:
    print('Você cancelou a operação.')
else:
    print('Você entrou com {0}'.format(texto))
