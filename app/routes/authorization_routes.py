from flask import jsonify, request, Flask
from utils.auth_service import Jwt_service
def register_routes_authorization(app: Flask):
    """
    Registra uma rota de teste para verificar o JWT 


    Esta funcao define um rota protegeda de teste ("/protected") que exije um token jwt válido
    para o acesso. Token deve ser fornecido no cabecalho de autorizacao (Authorization) com o prexo "Bearer". 
    
    Caso o token seja inválido, ausente ou expeirado o acesso será negado.
    
    Args:
        app (Flask): a estancia do aplicativo Flask on a rotá seá registrada

    Returns:
        Response: Retorna um resposta JSON com um menssage de sucesso ou erro juntamente com o codigo de status HTTP correspondente
    """
    
    @app.route("/protected", methods=["GET"])
    def protected_router():
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Token não fornecido"})
            
        token = auth_header.split(" ")[1]

        payload = Jwt_service.decode_jwt(token)

        if not payload:
            return jsonify({"error": "Token inválido ou expirado"}), 401
        
        return jsonify({"message": "Acesso concedido", "user": payload["sub"]}), 200