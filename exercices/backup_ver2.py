# -*- coding: utf-8 -*-
import os
import time

origem = ["/home/calazans/Studies/"]

dir_alvo = "/home/calazans/Backup"

hoje = dir_alvo + os.sep + time.strftime("%Y%m%d")
agora = time.strftime("%H%M%S")

if not os.path.exists(hoje):
    os.mkdir(hoje)
    print('Bem-sucedida Criação do diretório', hoje)

alvo = hoje + os.sep + agora + ".zip"

comando_zip = "zip -qr {0} {1}".format(alvo, ' '.join(origem))

if os.system(comando_zip) == 0:
    print('Backup bem-sucedido em', alvo)
else:
    print('Backup FALHOU')
