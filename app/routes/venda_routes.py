from flask import jsonify, request, Flask
from service.venda_service import Service_venda
from decorators.jwt_required import jwt_required
from utils.json_validator import Validator

def register_venda_routes(app: Flask):
    
    @app.route("/cadastro/venda", methods=["POST"])
    @jwt_required
    def insert_venda():
        try:

            json_venda = request.get_json()
            
            if json_venda:
            
                if Validator.venda_json(json_venda):
                    venda = Service_venda.insert_venda(json_venda)
                    
                    return jsonify({'message': "venda cadastrada"}), 201
                else:
                    return  jsonify({'message': "venda não cadastrada"}), 402
            else:
                return jsonify({"error": "json não identificado"}), 400
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
            if id_venda:
                venda = Service_venda.filter_vendas(id_venda)
                return jsonify({"mensage": Service_venda.filter_vendas(id_venda)})
            else:
                return jsonify({"error": "argumentos não identificados"}), 400
        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400
    
    @app.route("/filtro/venda-data", methods = ['GET'])
    def filtro_venda_data():
        try:
            data_venda: str = request.args.get("data_venda")
            if data_venda:
                return jsonify({"mensage": Service_venda.filter_date_vendas(data_venda)})
            else:
                return jsonify({"error": "argumentos não identificados"})
        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400
    
    @app.route('/delete/venda', methods = ['POST'])
    def exluir_venda():
        
        try:
            
            id_venda = request.args.get("id_venda")
            
            if id_venda:
                
                return jsonify({"message": Service_venda.delete_venda(id_venda)})
            
            else:
                return jsonify({"error": "argumentos não identificados"})
        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400
    
    @app.route('/cancel/venda', methods = ['POST'])
    def cancelar_venda():
        
        try:
            id_venda: int = request.args.get("id_venda")
            if id_venda:
                return jsonify({"message": Service_venda.cancel_venda(id_venda)})
            else:
                return jsonify({"error": "argumentos não identificados"})
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
            if json_venda:
                validacao_json_vendas = Validator.venda_json(json_venda)

                if validacao_json_vendas['status']:

                    transacao_venda: dict = Service_venda.sale_venda(json_venda)

                    if transacao_venda['status']:
                        return jsonify({'message': transacao_venda['message']}), 201

                    else:
                        return jsonify({'message': transacao_venda['message'], 'status': transacao_venda["status_elemento"]}), 400

                else:
                    return  jsonify({'message': validacao_json_vendas["message_error"]}), 400
                
            else:
                return jsonify({"error": "argumentos não identificado"})
            
        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400