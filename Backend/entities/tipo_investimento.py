from pony.orm import PrimaryKey, Required, Set
from env.db import db

class TipoInvestimento(db.Entity):
    _table_ = 'tipos_investimentos'
    id = PrimaryKey(int, auto=True)
    descricao = Required(str, 255)
    descricao_abreviada = Required(str, 50)
    
    titulos = Set('TipoTitulo')
    distruicoes_investimentos = Set('DistribuicaoInvestimento')