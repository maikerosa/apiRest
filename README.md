Esse projeto é uma apiRest para o gerenciamento de uma livraria, onde é possível cadastrar, atualizar, deletar e listar os livros, autores e editoras.

-- Simple API Rest

Para python > 3:

File "C:\Users\mk\Documents\Projetos\apiRest\env\lib\site-packages\flask_restplus\model.py", line 8, in <module>
from collections import OrderedDict, MutableMapping

Edição:

from collections import OrderedDict

import sys

if sys.version_info[:2] >= (3, 8):
    from collections.abc import MutableMapping
else:
    from collections import MutableMapping
