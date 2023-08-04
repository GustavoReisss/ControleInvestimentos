from pony.orm import db_session
from pony.orm.core import ObjectNotFound
from repositories.BaseRepository import BaseRepository
from entities import User, DistribuicaoInvestimento
from env.db import db
from collections import namedtuple


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(entity=User)
        self.distribuicao_repository = BaseRepository(DistribuicaoInvestimento)
    
    @db_session
    def get_distribuicoes(self, user_id):
        
        query = """
            SELECT
                t2.id AS distribuicao_id,
                t1.descricao,
                t1.id AS tipo_investimento_id,
                coalesce(t2.porcentagem, 0) AS 'porcentagem'
            FROM tipos_investimentos AS t1
            LEFT JOIN (
                SELECT * FROM distribuicao_investimento WHERE user_id = $id_usuario
            ) AS t2
            ON t1.id = t2.tipo_investimento_id
        """
        
        # Define a estrutura da linha de resultados como uma namedtuple
        ResultRow = namedtuple('ResultRow', ['distribuicao_id', 'descricao', 'tipo_investimento_id', 'porcentagem'])

        # Executa a consulta SQL e obtém os resultados
        data = db.execute(sql=query, globals={"id_usuario": user_id}).fetchall()

        # Transforma os resultados em uma lista de dicionários
        result_list = [ResultRow(*row)._asdict() for row in data]

        return result_list
    
    def create_distribuicao(self, distribuicao: dict):
        entity_to_save = {
            "porcentagem": distribuicao["porcentagem"],
            "tipo_investimento_id": distribuicao["tipo_investimento_id"],
            "user_id": 1
        }

        if not DistribuicaoInvestimento.exists(tipo_investimento_id=distribuicao["tipo_investimento_id"], user_id=1):
            self.distribuicao_repository.create(entity_to_save)

    
    @db_session
    def update_distribuicoes(self, data: list[dict]):
        self.entity = DistribuicaoInvestimento
        
        for distribuicao in data:
            id = distribuicao["distribuicao_id"]
            
            if id is None:
                self.create_distribuicao(distribuicao)
                continue
            
            try:
                DistribuicaoInvestimento[id].set(porcentagem=distribuicao["porcentagem"])
            except ObjectNotFound:
                print("objeto com id %d não encontrado, tentando criar uma nova distribuicao caso não exista" % id)
                self.create_distribuicao(distribuicao)

        return self.get_distribuicoes(1)