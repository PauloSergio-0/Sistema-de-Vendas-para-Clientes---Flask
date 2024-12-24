from flask import jsonify, request, Flask
from service.venda_service import Service_venda
from decorators.jwt_required import jwt_required
from utils.json_validator import Validator

def register_venda_routes(app: Flask):
    
    @app.route("/cadastro/venda", methods=["POST"])
    # @jwt_required
    def insert_venda():
        try:

            json_venda = request.get_json()
            
            if not json_venda:
                return jsonify({"error": "json não identificado"}), 400
            
            venda_valited = Validator.venda_json(json_venda)
            if not venda_valited['status']:
                return  jsonify({'message': venda_valited['message_error']}), 400

            venda = Service_venda.sale_venda(json_venda)
            if venda['status']:
                return jsonify({'message': venda['message']}), 201
            else:
                return jsonify({'error': venda['message_error']}), 400
                

        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400
    
    @app.route("/listar/venda", methods=['GET'])
    def listar_venda():
        
        try:
            
            lista_venda = Service_venda.list_venda()
            if lista_venda['status']:
                return jsonify({"vendas": lista_venda['content']})
            
            else:
                return jsonify({"error": f"Não é possivel concluir operação: {lista_venda['message_error']}"})
                
        
        except Exception as e:
            return jsonify({"error": f"Não foi possivel concluir serviço: {e}"}), 401
            
    
    @app.route("/filtro/venda", methods = ['GET'])
    def filtro_venda():
        try:
            id_venda = request.args.get("id_venda")
            
            if not id_venda:
                return jsonify({"error": "argumentos não identificados"}), 400
            
            venda = Service_venda.filter_vendas(int(id_venda))
            if venda['status']:
                return jsonify({"mensage": venda['content']}), 200
            else:
                return jsonify({"error": venda['message_error']}), 400
                

                
        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400
    
    @app.route("/filtro/venda-data", methods = ['GET'])
    def filtro_venda_data():
        try:
            data_venda: str = request.args.get("data_venda")
            if not data_venda:
                return jsonify({"error": "argumentos não identificados"}), 400
            
            venda = Service_venda.filter_date_venda(str(data_venda))
            if venda['status']:
                return jsonify({"mensage": venda['content']}), 200
            else:
                return jsonify({"error": venda['message_error']}), 400
            
        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400
    
    @app.route('/delete/venda', methods = ['PATCH'])
    def exluir_venda():
        
        try:
            
            id_venda = request.args.get("id_venda")
            
            if not id_venda:
                return jsonify({"error": "argumentos não identificados"})
            
            venda = Service_venda.delete_venda(int(id_venda))
            if venda['status']:
                return jsonify({"message": venda['message']}), 200
            else:
                return jsonify({"error": venda['message_error']}), 400
            

        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400
    
    @app.route('/cancel/venda', methods = ['PUT'])
    def cancelar_venda():
        
        try:
            id_venda: int = request.args.get("id_venda")
            if not id_venda:
                return jsonify({"error": "argumentos não identificados"})
            
            venda = Service_venda.cancel_venda(int(id_venda))
            if venda['status']:
                return jsonify({"message": venda['message']}), 200
            else:
                return jsonify({"error": venda['message_error']}), 400
                

        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400
            
            
    @app.route('/sale/venda', methods = ['POST'])
    def realzar_venda():
        """
            Esta rota é responsavel por realizar a venda verificando a existencia do cliente e produto e 
            se sao aptos para o prosseguimento da venda
        """
        try:
            json_venda = request.get_json()
            if not json_venda:
                return jsonify({"error": "argumentos não identificado"}),400
            
            validacao_json_vendas = Validator.venda_json(json_venda)
            
            if not validacao_json_vendas['status']:
                return jsonify({'message': validacao_json_vendas["message_error"]}), 400

            

            transacao_venda = Service_venda.insert_venda(json_venda)
            
            if  transacao_venda['status']:
                return jsonify({'message': transacao_venda['message']}), 201

            else:
                return jsonify({'message': transacao_venda['message_error'], 'status': transacao_venda["status_elemento"]}), 400

        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400