from flask import jsonify, request, Flask
from service.venda_service import Service_venda
from decorators.jwt_required import jwt_required
from utils.json_validator import Validator

def register_venda_routes(app):
    
    @app.route("/cadastro/venda", methods=["POST"])
    @jwt_required
    def insert_venda():
        json_venda = request.get_json()
        print(json_venda)
        
        if Validator.venda_json(json_venda):
            Service_venda.insert_venda(json_venda)
            
        return jsonify({'message': "venda cadastrado"}), 201
    
    @app.route("/listar/venda", methods=['GET'])
    def listar_venda():
        return Service_venda.list_venda()