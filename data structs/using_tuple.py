# -*- coding: utf-8

zoo = ('lobo', 'elefante', 'pinguim',)
print('O número de animais no zoo é', len(zoo))

novo_zoo = ('macaco', 'golfinho', zoo,)
print('O número de animais no novo zoo é', len(novo_zoo))
print('Todos os animais no novo zoo são', novo_zoo)
print('Os animais trazidos do antigo zoo são', novo_zoo[2])
print('O último animal trazido do antigo zoo é', novo_zoo[2][2])
