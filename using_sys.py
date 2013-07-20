# -*- coding: utf-8 -*-
import sys

print('Os argumentos da linha de comando são:')

for i in sys.argv:
    print(i)

print('\n\nO PYTHONPATH é', sys.path, '\n')
