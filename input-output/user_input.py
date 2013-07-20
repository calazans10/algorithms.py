# -*- coding: utf-8 -*-
import re
import unicodedata


def reverse(texto):
    return texto[::-1]


def normalize(texto):
    texto = unicode(texto)
    normalize = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore')
    normalize = str(normalize)
    normalize = re.sub('[-,!]', "", normalize.replace(" ", "").lower())

    return normalize


def is_palindrome(texto):
    texto = normalize(texto)

    return texto == reverse(texto)

algo = u"Socorram-me, subi no ônibus em marrocos"

if is_palindrome(algo):
    print('Sim, é um palíndromo')
else:
    print('Não, não é um palíndromo')
