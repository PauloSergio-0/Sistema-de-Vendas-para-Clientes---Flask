from flask import jsonify

# TODO: ajustar  validadores para uma dict
class Validator:
    
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
        
        print(json)
        for keys, values in json.items():
            
            if keys not in keys_json_venda:
                return {"status": False, "message_error": f"A chave '{keys}' não é válida para o serviço."}
            
            if (values == type(int) and values is None) or ( values == type(str) and not values.strip()):
                return {"status": False, "message_error": f"A chave '{keys}' está com o valor vázio."}
                
            
        
        return {"status": True}
        
