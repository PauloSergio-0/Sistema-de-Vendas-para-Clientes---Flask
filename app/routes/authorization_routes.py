from flask import jsonify, request
from utils.auth_service import Jwt_service

def register_routes_authorization(app):
    
    @app.route("/protected", methods=["GET"])
    def protected_router():
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Token não fornecido"})
            
        token = auth_header.split(" ")[1]

        payload = Jwt_service.decode_jwt(token)

        if not payload:
            return jsonify({"error": "Token inválido ou expirado"}), 401
        
        return jsonify({"message": "Acesso concedido", "user": payload["sub"]})