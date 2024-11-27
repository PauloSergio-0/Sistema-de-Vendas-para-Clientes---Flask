from flask import request, jsonify
from utils.json_validator import Validator
from service.cliente_service import Service_cliente
from decorators.jwt_required import jwt_required


def register_clientes_routes(app):
    
    @app.route('/cadastro/clientes', methods = ['POST'])
    @jwt_required
    def cadastrar_clientes():
        json_cliente = request.get_json()
        print('json_cliente')
        print(json_cliente)
        if Validator.cliente_json(json_cliente):
            Service_cliente.insert_cliente(json_cliente)
        return jsonify({"mensage": "cliente cadastrado"}), 201
    
