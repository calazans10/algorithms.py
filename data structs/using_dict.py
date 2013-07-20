# -*- coding: utf-8 -*-

ab = {'Jeferson': 'calazans10@gmail.com',
      'Allan': 'allan@gmail.com',
      'Sasha': 'sasha@gmail.com',
      'Steve': 'steve@gmail.com'}

print("Jeferson's address is", ab['Jeferson'])

del ab['Steve']

print('\nThere are {0} contacts in the address book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {0} at {1}'.format(name, address))

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])
