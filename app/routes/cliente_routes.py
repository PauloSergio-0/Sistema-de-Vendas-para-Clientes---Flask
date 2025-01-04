from flask import request, jsonify, Flask, current_app
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
            integridade do conteudo ex: tipo, formato e valides do campo, tambem com a capacidade de retornar o erro em
            especifico facilitando a manutenção em caso de falhas.
            
            Caso o JSON seja valido elo pasa para a fase de inserção de dados no banco pelo metodo 'Service_cliente.insert_cliente()'
        """
        
        try:
            
            #adciona log
            app.logger.info("cadastrou clientes")
            
            json_cliente = request.get_json()
            if not json_cliente:
                return jsonify({"error": "JSON não recebido"}), 400
            
            validador_json_cliente = Validator.cliente_json(json_cliente)
            if not validador_json_cliente["status"]:
                return jsonify({"error": validador_json_cliente["message_error"]}), 400
            
            cliente = Service_cliente.insert_cliente(json_cliente)
            if cliente['status']:
                return jsonify({"mensage": cliente['message']}), 201
            else:
                return jsonify({"error": cliente['message_error']}), 400

        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400

    @app.route('/listar/cliente', methods = ['GET'])
    def listar_cliente():
        """
            Rota para listar todos os clientes do banco de dados.
            
            Retorna  ativos, inativos e excluidos.
        """
        try:
            #adciona log
            app.logger.info("Obteve lista de clientes")
            
            lista_cliente = Service_cliente.list_cliente()
            if lista_cliente['status']:
                return jsonify({"cliente": lista_cliente['content']}), 200
            else:
                return jsonify({"error": lista_cliente['message_error']}), 400
            
        except Exception as e:
                return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400
    
    @app.route("/filtro/cliente", methods = ['GET'])
    def filtro_cliente():
        """
            Rora para exibir cliente pelo seu 'id' que deve ser recebido via parametro

            Retorno o cliente de acordo com a id selecionada.
        """
        try:
            
            id_cliente = request.args.get('id_cliente')
            
            #adciona log
            app.logger.info(f"tentativa de filtrar cliente com id {id_cliente}")
            
            if not id_cliente:
                return jsonify({"message": "Não foi possivel identificar argumentos"}), 400
            
            cliente = Service_cliente.filter_cliente(int(id_cliente))
            if cliente['status']:
                return jsonify({"message": cliente['content']}),200
            else:
                return jsonify({"error": cliente['message_error']}),400
            
        except Exception as e:
            return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400
    
    @app.route("/delete/cliente", methods = ['PATCH'])
    def delete_cliente():
        
        """
        Rota para deletar de forma lógica um cliente pelo seu id
            Retorna a mensagem de cofirmação de cliente excluido 
        """
        try:
            id_cliente = request.args.get("id_cliente")
            
            #log
            app.logger.info(f"tentativa de deletar cliente com id {id_cliente}")

            if  not id_cliente:
                
                return jsonify({"message": "Não foi possivel identificar argumentos"}), 400
            
            cliente = Service_cliente.delete_cliente(int(id_cliente))
            if cliente['status']:
                return jsonify({"message": cliente['message']}),201
            
            else:
                return jsonify({"error": cliente['message_error']}), 400
                
            
        except Exception as e:
            return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400
        
    @app.route("/desactivate/cliente", methods = ['PUT'])
    def desativar_cliente():
        """
            Rota para desativatr de forma lógica desactivate um cliente pelo seu id

            RetRetorna a mensagem de cofirmação de cliente desativado
        """

        try:

            id_cliente = request.args.get("id_cliente")

            #log
            app.logger.info(f"tentativa de desativar cliente com id {id_cliente}")

            if not id_cliente:
                return jsonify({"message": "Não foi possivel identificar argumentos"}), 400
            
            cliente = Service_cliente.desactivate_cliente(int(id_cliente))
            if cliente['status']:
                return jsonify({"message": cliente['message']}), 201
            
            else:
                return jsonify({"error": cliente['message_error']}), 400

        except Exception as e:
            return jsonify({"error": f"Não foi possível concluir o serviço devido o erro: {e}"}), 400