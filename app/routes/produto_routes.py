from flask import jsonify, request, Flask
from service.produto_service import Service_produto
from decorators.jwt_required import jwt_required
from utils.json_validator import Validator

def register_produto_routes(app):
    
    @app.route("/cadastro/produto", methods=["POST"])
    @jwt_required
    def insert_produto():
        
        json_produto = request.get_json()
        
        if Validator.produto_json(json_produto):
            Service_produto.insert_produto(json_produto)
            
        return jsonify({'message': "produto cadastrado"}), 201