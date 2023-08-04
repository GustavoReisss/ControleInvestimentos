from pony.orm import PrimaryKey, Required, Set
from env.db import db

class TipoUser(db.Entity):
    _table_ = "tipo_usuario"
    id = PrimaryKey(int, auto=True)
    nome = Required(str)
    titulos = Set('User')
    