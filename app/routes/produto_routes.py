from flask import jsonify, request, Flask
from service.produto_service import Service_produto
from decorators.jwt_required import jwt_required
from utils.json_validator import Validator

def register_produto_routes(app:Flask):
    
    @app.route("/cadastro/produto", methods=["POST"])
    @jwt_required
    def insert_produto():
        try:
            json_produto = request.get_json()
            
            if json_produto:
                validador_json_produto = Validator.produto_json(json_produto)
                if validador_json_produto["status"]:
                    Service_produto.insert_produto(json_produto)
                    
                    return jsonify({'message': "produto cadastrado"}), 201
                
                else:
                    return jsonify({"error": validador_json_produto["message_error"]}),400
            else:
                return jsonify({"error": "JSON não recebido"}),400
        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400
    @app.route("/listar/produto", methods = ['GET'])
    def listar_produto():
        
        return jsonify({"message": Service_produto.list_produto()}),200

    @app.route('/filtro/produto', methods = ['GET'])
    def filtro_produto():

        try:

            id_produto = request.args.get('id_produto')

            if id_produto:

                return jsonify({'message': Service_produto.filter_produto(id_produto)}),201

            else:
                    return jsonify({"error": "JSON não recebido"}),400
                
        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400
    
    @app.route('/delete/produto', methods = ['GET'])
    def exlcluir_produto():
        
        try:
            id_produto = request.args.get("id_produto")
            if id_produto:
                return jsonify({"message": Service_produto.delete_produto(id_produto)})
            else:
                    return jsonify({"error": "JSON não recebido"}),400
        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400


    @app.route('/desactivate/produto', methods = ['GET'])
    def desativar_produto():
        
        try:
            
            id_produto = request.args.get("id_produto")

            if id_produto:
                return jsonify({"message": Service_produto.desactivate_produto(id_produto)})
            
            else:
                return jsonify({"error": "JSON não recebido"}),400
        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400