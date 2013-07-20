# -*- coding: utf-8 -*-


class Person:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print('Olá, meu nome é', self.name)

p = Person('Jeferson')
p.sayHi()
