from pony.orm import PrimaryKey, Required, Set
from env.db import db
from .tipo_user import TipoUser

class User(db.Entity):
    _table_ = "users"
    id = PrimaryKey(int, auto=True)
    tipo_usuario_id = Required(TipoUser)
    username = Required(str)
    email = Required(str)
    password = Required(str)
    distruicoes_investimentos = Set('DistribuicaoInvestimento')