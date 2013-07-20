# -*- coding: utf-8 -*-
import os
import time

origem = ["/home/calazans/Studies/"]

dir_alvo = "/home/calazans/Backup"

alvo = dir_alvo + os.sep + time.strftime("%Y%m%d%H%M%S") + '.zip'

comando_zip = "zip -qr {0} {1}".format(alvo, ' '.join(origem))

if os.system(comando_zip) == 0:
    print('Backup bem-sucedido em', alvo)
else:
    print('Backup FALHOU')
