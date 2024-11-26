from flask import jsonify

class Validator:
    
    def cliente_json(json:dict):
        
        keys_json_clientes = {'id', 'nome', 'endereco', 'contato'}
        
        for keys, values in json.items():
            
            if keys not in keys_json_clientes :
                raise jsonify({"erro": f"A chave '{keys}' não é válida para o serviço."})
            
            if  values is None:
                raise jsonify({"erro": f"A chave '{keys}' está com o valor vázio."})
            
            else:
                return True
            
