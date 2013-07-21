# -*- coding: utf-8 -*-
import time


try:
    f = open('poema.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end=" ")
        time.sleep(2)
except KeyboardInterrupt:
    print('!! Você cancelou a leitura do arquivo.')
finally:
    f.close()
    print('(Limpando tudo: Fechando o arquivo)')
