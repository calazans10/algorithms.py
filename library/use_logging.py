# -*- coding: utf-8 -*-
import os
import platform
import logging


if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('DIRETÓRIOINICIAL'),
                                os.getenv('CAMINHO'), 'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s: %(levelname)s: %(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug("Início do programa")
logging.info("Fazendo alguma coisa")
logging.warning("Terminando agora")
