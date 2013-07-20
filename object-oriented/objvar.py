# -*- coding: utf-8 -*-


class Robot:
    '''Representa um robô com um nome.'''

    population = 0

    def __init__(self, name):
        self.name = name
        print('(Iniciando {0})'.format(self.name))

        Robot.population += 1

    def __del__(self):
        '''Estou morrendo'''
        print('{0} sendo destruído'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{0} era o último'.format(self.name))
        else:
            print('Existe(m) ainda {0:d} robô(s) trabalhando'.format(
                Robot.population))

    def sayHi(self):
        '''Saudações do robô.
        Sim, eles podem fazer isso.'''
        print('Saudações, meus mestres me chamam {0}'.format(self.name))

    @classmethod
    def howMany(klass):
        '''Imprime a população atual.'''
        print('Temos um total de {0:d} robô(s)'.format(Robot.population))

droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()

droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()

print('\nRobôs podem realizar algum trabalho aqui.\n')

print('Robôs terminaram seus trabalhos. Então vamos destruí-los.')

del droid1
del droid2

Robot.howMany()
