from flask import jsonify
from datetime import datetime


class Validator:

    """
        Esta classe é respónsavel por conter um conjunto de validadores dos JSONs recebidos para prosseguir com
        a execuções das rotas.
        
        Retornar dois valores um boleano (True ou False) 
        
        caso encontre um erro retorna False em conjunto com uma mendagem de erro para especificalo
    """

    def _is_Date(string: str, date_format = "%Y-%m-%d"):
        
        """
            Para verificar se o valor está do formato de data  

            retorna um boleano necessario para a valides do coteudo do JSON
        """
        
        try:
            datetime.strptime(string, date_format)
            return True

        except ValueError:
            return False

    def cliente_json(json:dict):

        keys_json_clientes = {'id', 'nome', 'endereco', 'contato'}

        for keys, values in json.items():

            if keys not in keys_json_clientes :
                return {"status": False, "message_error": f"A chave '{keys}' não é válida para o serviço."}

            if  (type(values) == int and keys == 'id') and (values is None or values < 1):
                return {"status": False, "message_error": f"A chave '{keys}' está com o valor menor que 1.  valor: {values}"}

            elif (type(values) == str and keys in {'nome', 'endereco', 'contato'}) and (values is None or not values.strip()):
                return  {"status": False, "message_error": f"A chave '{keys}' está com o valor vazio."}

            elif (type(values) == int and not keys == 'id') or (type(values) == str and not keys in {'nome', 'endereco', 'contato'}):
                return {"status": False, "message_error": f"A chave '{keys}' está com o valor do tipo {type(values)}."}

        return {"status": True}

    def produto_json(json: dict):

        keys_json_produto = {"id", "nome", "codigo", "categoria", "preco"}

        for keys, values in json.items():

            if keys not in keys_json_produto:
                return {"status": False, "message_error": f"A chave '{keys}' não é válida para o serviço."}

            if  (type(values) == int and keys == "id") and (values is None or values < 1):
                return {"status": False, "message_error": f"A chave '{keys}' está com o valor menor que 1.  valor: {values}"}

            elif (type(values) == str and keys in {"nome", "codigo", "categoria"}) and (values is None or not values.strip()):
                return {"status": False, "message_error": f"A chave '{keys}' está com o valor vazio."}

            elif (type(values) == float and keys == 'preco') and (values is None or values < 0):
                return {"status": False, "message_error": f"A chave '{keys}' está com o valor menor que 0.  valor: {values}"}

            elif (type(values) == str and not keys in {"nome", "codigo", "categoria"}) or (type(values) == int and not keys == 'id') or (type(values) == float and not keys == 'preco'):
                return {"status": False, "message_error": f"A chave '{keys}' está com o valor do tipo {type(values)}."}

        return {"status": True}

    def venda_json(json: dict):

        keys_json_venda = {"id_cliente", "id_produto", "qtd", "data"}
        
        keys_INT_json_venda = {"id_cliente", "id_produto", "qtd"}

        for keys, values in json.items():

            if keys not in keys_json_venda:
                return {"status": False, "message_error": f"A chave '{keys}' não é válida para o serviço."}

            if type(values) == int and (values is None or values < 1) and keys in keys_INT_json_venda:
                return {"status": False, "message_error": f"A chave '{keys}' está com o valor vázio ou com número inválido."}

            elif type(values) == str and keys == 'data' and not values.strip():
                return {"status": False, "message_error": f"A chave '{keys}' está com o valor vázio."}

            elif type(values) == str and keys == 'data' and not Validator._is_Date(string = values):
                return {"status": False, "message_error": f"A chave '{keys}' está no formato errado. valor: {values}"}

            elif (keys in keys_INT_json_venda and type(values) == str) or (keys not in keys_INT_json_venda and type(values) == int):
                return {"status": False, "message_error": f"A chave '{keys}' está com o valor do tipo {type(values)}."}

        return {"status": True}
    