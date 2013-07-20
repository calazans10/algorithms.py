# -*- coding: utf-8 -*-

number = 23
guess = int(input('Entre com um número inteiro: '))

if guess == number:
    print('Parabéns, você advinhou.')
    print('(mas você não ganhou nenhum prêmio!)')
elif guess < number:
    print('Não, era um pouco maior que isso')
else:
    print('Não, era um pouco menor que isso')

print('Feito')
