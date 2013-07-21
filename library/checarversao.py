# -*- coding: utf-8 -*-
import sys
import warnings


if sys.version_info[0] < 3:
    warnings.warn("Necessário Python 3.0 para rodar este programa",
                  RuntimeWarning)
else:
    print("Prosseguir normalmente")
