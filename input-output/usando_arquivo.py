# -*- coding: utf-8 -*-

poema = '''\
Programar é divertido
Quando o trabalho está pronto
se você quer tornar seu trabalho divertido:
    use Python!'''

f = open('poema.txt', 'w')
f.write(poema)
f.close()

f = open('poema.txt')
while True:
    linha = f.readline()
    if len(linha) == 0:
        break
    print(linha, end="")
f.close()
