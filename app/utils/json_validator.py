from flask import jsonify
from datetime import datetime


# TODO: ajustar  validadores para uma dict
class Validator:

    def _is_Date(string: str, date_format = "%Y-%m-%d"):
        
        try:
            datetime.strptime(string, date_format)
            return True
        except ValueError:
            return False
    
    
    
    def cliente_json(json:dict):
        
        keys_json_clientes = {'id', 'nome', 'endereco', 'contato'}
        
        for keys, values in json.items():
            
            if keys not in keys_json_clientes :
                raise jsonify({"error": f"A chave '{keys}' não é válida para o serviço."})
            
            if  values is None:
                raise jsonify({"error": f"A chave '{keys}' está com o valor vázio."})
            

        return True
            
    def produto_json(json: dict):
        
        keys_json_produto = {"id", "nome", "Codigo", "categoria", "preco"}
        
        for keys, values in json.items():
            
            if keys not in keys_json_produto:
                return jsonify({"error": f"A chave '{keys}' não é válida para o serviço."}), 401
            
            if values is None:
                return jsonify({"error": f"A chave '{keys}' está com o valor vázio."})
            
            
        return True
            
    def venda_json(json: dict):
        
        keys_json_venda = {"id_cliente", "id_produto", "qtd", "data"}
        keys_INT_json_venda = {"id_cliente", "id_produto", "qtd"}
        
        
        for keys, values in json.items():
            
            if keys not in keys_json_venda:
                return {"status": False, "message_error": f"A chave '{keys}' não é válida para o serviço."}
            print(keys, values, type(values))
            print(f'data: {Validator._is_Date(string =str(values))}')
            
            if type(values) == int and (values is None or values < 1) and keys in keys_INT_json_venda:
                return {"status": False, "message_error": f"A chave '{keys}' está com o valor vázio ou com número inválido."}
            
            elif type(values) == str and (not values.strip()) and keys == 'data' and not Validator._is_Date(string =values):
                return {"status": False, "message_error": f"A chave '{keys}' está com o valor vázio ou no formato errado.\n valor: {values}"}
                
            elif (keys in keys_INT_json_venda and type(values) == str) or (keys not in keys_INT_json_venda and type(values) == int):
                return {"status": False, "message_error": f"A chave '{keys}' está com o valor do tipo {type(keys)}."}
            
            
        
        return {"status": True}
        
