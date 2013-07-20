# -*- coding: utf-8 -*-

print('Atribuição Simples')
shoplista = ['maçã', 'manga', 'arroz', 'banana']
minhalista = shoplista

del shoplista[0]

print('shoplista é', shoplista)
print('minhalista é', minhalista)

print('Copie por meio de uma fatia completa')
minhalista = shoplista[:]

del minhalista[0]

print('shoplista é', shoplista)
print('minhalista é', minhalista)
