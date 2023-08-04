from pony.orm import PrimaryKey, Required
from env.db import db
from .tipo_investimento import TipoInvestimento

class TipoTitulo(db.Entity):
    _table_ = "tipos_titulos"
    id = PrimaryKey(int, auto=True)
    tipo_investimento_id = Required(TipoInvestimento)
    descricao = Required(str)