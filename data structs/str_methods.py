# -*- coding: utf-8 -*-

nome = 'Jeferson'

if nome.startswith('Jef'):
    print('Sim, a string começa com "Jef"')

if 'e' in nome:
    print('Sim, ela também contém a string "e"')

if nome.find('son') != -1:
    print('Sim, ela contém a string "son"')

delimitador = '_*_'

minhalista = ['Brasil', 'Russia', 'Índia', 'China']
print(delimitador.join(minhalista))
