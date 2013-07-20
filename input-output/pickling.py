# -*- coding: utf-8 -*-
import pickle


arquivo_listadecompras = 'listadecompras.data'
listadecompras = ['maçã', 'manga', 'cenoura']

f = open(arquivo_listadecompras, 'wb')
pickle.dump(listadecompras, f)
f.close()

f = open(arquivo_listadecompras, 'rb')
lista_armazenada = pickle.load(f)
print(lista_armazenada)
