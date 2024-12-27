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
            
            if not json_produto:
                return jsonify({"error": "JSON não recebido"}),400
            
            validador_json_produto = Validator.produto_json(json_produto)
            if not validador_json_produto["status"]:
                return jsonify({"error": validador_json_produto["message_error"]}),400
            
            produto = Service_produto.insert_produto(json_produto)
            if produto['status']:
                return jsonify({'message': produto['message']}), 201
            
            else:
                return jsonify({'error': produto['message_error']}), 400
            
        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400
            
    @app.route("/listar/produto", methods = ['GET'])
    def listar_produto():
        try:
            
            produto =  Service_produto.list_produto()
            
            if produto['status']:
                return jsonify({"message": produto['content']}), 200
            else:
                return jsonify({"error": produto['message_error']}), 400
            
        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400
            

    @app.route('/filtro/produto', methods = ['GET'])
    def filtro_produto():
        try:

            id_produto = request.args.get('id_produto')

            if not id_produto:
                    return jsonify({"error": "JSON não recebido"}),400

            produto = Service_produto.filter_produto(int(id_produto))
            if produto['status']:
                return jsonify({'message': produto['content']}), 200
            else:            
                return jsonify({'error': f"error no serviço: {produto['message_error']}"}), 400

        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400
    
    @app.route('/delete/produto', methods = ['PATCH'])
    def exlcluir_produto():
        
        try:
            id_produto = request.args.get("id_produto")
            if not id_produto:
                    return jsonify({"error": "Parametro não recebido"}), 400
                
            produto = Service_produto.delete_produto(int(id_produto))
            if produto['status']:
                return jsonify({"messsage": produto['message']}), 201
            else:
                return jsonify({'error': produto['message_error']}), 400
            
        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400


    @app.route('/desactivate/produto', methods = ['PUT'])
    def desativar_produto():
        
        try:
            
            id_produto = request.args.get("id_produto")

            if not id_produto:
                return jsonify({"error": "JSON não recebido"}), 400
            
            produto = Service_produto.desactivate_produto(int(id_produto))
            if produto['status']:
                return jsonify({'message': produto['message']}), 201
            
            else:
                return jsonify({'error': produto['message_error']}), 400
                
        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400