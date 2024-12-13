from flask import jsonify, request
from utils.auth_service import Jwt_service
from functools import wraps

def jwt_required(f):
    
    @wraps(f)
    
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Token não fornecido"}), 401
            
        token = auth_header.split(" ")[1]
    
        payload = Jwt_service.decode_jwt(token)

        if not payload:
            return jsonify({"error": "Token inválido ou expirado"}), 401
        
        request.user = payload
        
        return f(*args, **kwargs)
    return decorated_function