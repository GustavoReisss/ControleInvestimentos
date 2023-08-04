from env.db import db

from .distribuicao_investimento import DistribuicaoInvestimento
from .tipo_investimento import TipoInvestimento
from .tipo_titulo import TipoTitulo
from .tipo_user import TipoUser
from .user import User

db.generate_mapping()
