from flask import (
    Flask,
    jsonify,
    request
)

from repositories.BaseRepository import BaseRepository
from repositories.UserRepository import UserRepository

from entities import (
    TipoInvestimento,
    TipoTitulo
)

import json

app = Flask(__name__)

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
    response.headers.add('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')
    return response

@app.route('/resumo', methods=['GET'])
def get_json():
    with open('./resultado.json', encoding="utf-8") as file:
        data = json.load(file)
    response = jsonify(data)
    return response

@app.route('/acoes', methods=['GET'])
def get_json2():
    with open('./acoes/acoes.json', encoding="utf-8") as file:
        data = json.load(file)
    response = jsonify(data)
    return response

@app.route('/distribuicoes', methods=['GET'])
def get_json3():
    data = UserRepository().get_distribuicoes(1)
    return jsonify(data)

@app.route('/distribuicoes', methods=['POST'])
def get_json4():
    data = UserRepository().update_distribuicoes(request.json)
    return jsonify(data)

class GenericRoute:
    def __init__(self, route, entity):
        self.route = route
        self.entity = entity
        self.repository = BaseRepository(entity)
        self.register_routes()

    def get_all(self):
        filters = request.args.to_dict()
        data = [item.to_dict() for item in self.repository.get_all(**filters)]
        return jsonify(data)

    def create(self):
        data = request.json
        new_item = self.entity(**data)
        self.repository.add(new_item)
        return jsonify(new_item.to_dict())

    def update(self):
        data = request.json
        item_id = data['id']
        item = self.repository.get(item_id)
        item.update(**data)
        return jsonify(item.to_dict())

    def delete(self):
        data = request.json
        item_id = data['id']
        item = self.repository.get(item_id)
        self.repository.delete(item)
        return jsonify({'message': 'Item deleted successfully'})

    def register_routes(self):
        app.add_url_rule(self.route, methods=['GET'], view_func=self.get_all, endpoint=f'{self.route}_get_all')
        app.add_url_rule(self.route, methods=['POST'], view_func=self.create, endpoint=f'{self.route}_create')
        app.add_url_rule(self.route, methods=['PUT'], view_func=self.update, endpoint=f'{self.route}_update')
        app.add_url_rule(self.route, methods=['DELETE'], view_func=self.delete, endpoint=f'{self.route}_delete')


def set_routes():
    GenericRoute('/tipos_investimentos', TipoInvestimento)
    GenericRoute('/tipos_titulos', TipoTitulo)

if __name__ == '__main__':
    set_routes()
    app.run(debug=True)
