# -*- coding: utf-8 -*-

shoplista = ['maçã', 'manga', 'cenoura', 'banana']

print('Eu tenho', len(shoplista), 'itens para comprar')

print('Estes itens são:', end=' ')
for item in shoplista:
    print(item, end=' ')

print('\nTambém tenho que comprar arroz.')
shoplista.append('arroz')
print('Minha lista de compras agora é', shoplista)

print('Vou colocar a minha lista em ordem agora')
shoplista.sort()
print('A minha lista ordenada é', shoplista)

print('O primeiro item que comprarei é', shoplista[0])
olditem = shoplista[0]
del shoplista[0]
print('Eu comprei o', olditem)
print('Minha lista de compras agora é', shoplista)
