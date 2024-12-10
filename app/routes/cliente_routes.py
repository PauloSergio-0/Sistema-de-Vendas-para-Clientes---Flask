from flask import request, jsonify, Flask
from utils.json_validator import Validator
from service.cliente_service import Service_cliente
from decorators.jwt_required import jwt_required


def register_clientes_routes(app: Flask):
    
    @app.route('/cadastro/cliente', methods = ['POST'])
    @jwt_required
    
    def cadastrar_clientes():
        """
            _summary_

            Rota protegida para a receber um JSON que seus dados serao inseridos no banco de dados
            
            Nesta rota recebe-se um JSON onde será válidado no metodo 'Validator.cliente_json()' onde vai verificar a 
            integridade do conteudo ex: tipo, formato e valides do campo, tambem com a capacidade de retornar o erro em especifico facilitando a manutenção em caso de falhas.
            
            Caso o JSON seja valido elo pasa para a fase de inserção de dados no banco de dados pelo metodo 'Service_cliente.insert_cliente()'
        """
        try:
            json_cliente = request.get_json()
            
            if json_cliente:
                
                validador_json_cliente = Validator.cliente_json(json_cliente)
                
                if validador_json_cliente["status"]:
                    Service_cliente.insert_cliente(json_cliente)
                    return jsonify({"mensage": "cliente cadastrado"}), 201
                
                else:
                    return jsonify({"error": validador_json_cliente["message_error"]}), 400

            else:
                    return jsonify({"error": "JSON não recebido"}), 400
        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviso devido o erro: {e}"}), 400
            
    

    @app.route('/listar/cliente', methods = ['GET'])
    def listar_cliente():
        """
            _summary_
        
        """
        return {"message": Service_cliente.list_cliente()}
    
    @app.route("/filtro/cliente", methods = ['GET'])
    def filtro_cliente():
        id_cliente = request.args.get('id_cliente')
        
        return jsonify({"message": Service_cliente.filter_cliente(id_cliente)})
    
    @app.route("/delete/cliente", methods = ['GET'])
    def delete_cliente():
        id_cliente = request.args.get("id_cliente")
        return jsonify({"message": Service_cliente.delete_cliente(id_cliente)})
    
    @app.route("/desactivate/cliente", methods = ['GET'])
    def desativar_cliente():
        id_cliente = request.args.get("id_cliente")
        return jsonify({"message": Service_cliente.desactivate_cliente(id_cliente)})