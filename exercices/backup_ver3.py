# -*- coding: utf-8 -*-
import os
import time

origem = ["/home/calazans/Studies/"]

dir_alvo = "/home/calazans/Backup"

hoje = dir_alvo + os.sep + time.strftime("%Y%m%d")
agora = time.strftime("%H%M%S")

coment = input('Entre com um comentário --> ')

if len(coment) == 0:
    alvo = hoje + os.sep + agora + ".zip"
else:
    alvo = hoje + os.sep + agora + "_" + coment.replace(' ', '_') + '.zip'

if not os.path.exists(hoje):
    os.mkdir(hoje)
    print('Bem-sucedida Criação do diretório', hoje)

comando_zip = "zip -qr {0} {1}".format(alvo, ' '.join(origem))

if os.system(comando_zip) == 0:
    print('Backup bem-sucedido em', alvo)
else:
    print('Backup FALHOU')
