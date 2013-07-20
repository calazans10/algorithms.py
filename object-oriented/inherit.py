# -*- coding: utf-8 -*-


class SchoolMember:
    '''Representa qualquer membro da escola.'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Iniciando SchoolMember: {0})'.format(self.name))

    def tell(self):
        '''Imprime os detalhes desta instância.'''
        print('Nome: "{0}" Idade: "{1}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    '''Representa um professor'''

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Iniciando Teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salário: "{0:d}"'.format(self.salary))


class Student(SchoolMember):
    '''Representa um aluno'''

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Iniciando Student: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Nota: "{0:d}"'.format(self.marks))

t = Teacher('Mrs. Sasha', 26, 1000000)
s = Student('Derek', 17, 75)

print()

members = [t, s]

for member in members:
    member.tell()
