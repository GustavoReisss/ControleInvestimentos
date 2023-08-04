from pony.orm import PrimaryKey, Required
from decimal import Decimal
from env.db import db
from .tipo_investimento import TipoInvestimento
from .user import User

class DistribuicaoInvestimento(db.Entity):
    _table_ = "distribuicao_investimento"
    id = PrimaryKey(int, auto=True)
    tipo_investimento_id = Required(TipoInvestimento)
    user_id = Required(User)
    porcentagem = Required(Decimal)