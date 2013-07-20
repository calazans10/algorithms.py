# -*- coding: utf-8 -*-

number = 23
running = True

while running:
    guess = int(input('Entre com um número inteiro: '))

    if guess == number:
        print('Parabéns, você advinhou.')
        running = False
    elif guess < number:
        print('Não, era um pouco maior que isso')
    else:
        print('Não, era um pouco menor que isso')

print('O loop while terminou.')
print('Fim')
