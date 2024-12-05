from flask import jsonify, request, Flask
from service.produto_service import Service_produto
from decorators.jwt_required import jwt_required
from utils.json_validator import Validator

def register_produto_routes(app:Flask):
    
    @app.route("/cadastro/produto", methods=["POST"])
    @jwt_required
    def insert_produto():
        
        json_produto = request.get_json()
        
        if Validator.produto_json(json_produto):
            Service_produto.insert_produto(json_produto)
            
        return jsonify({'message': "produto cadastrado"}), 201
    
    @app.route("/listar/produto", methods = ['GET'])
    def listar_produto():
        
        return jsonify({"message": Service_produto.list_produto()})
    
    
    @app.route('/filtro/produto', methods = ['GET'])
    def filtro_produto():
        
        id_produto = request.args.get('id_produto')
        return jsonify({'message': Service_produto.filter_produto(id_produto)})
    
    @app.route('/delete/produto', methods = ['GET'])
    def exlcluir_produto():
        id_produto = request.args.get("id_produto")
        return jsonify({"message": Service_produto.delete_produto(id_produto)})


    @app.route('/desactivate/produto', methods = ['GET'])
    def desativar_produto():
        id_produto = request.args.get("id_produto")
        return jsonify({"message": Service_produto.desactivate_produto(id_produto)})