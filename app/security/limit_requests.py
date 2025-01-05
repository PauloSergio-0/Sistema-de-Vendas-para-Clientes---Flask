from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import Flask, jsonify

limiter = Limiter(
    key_func= get_remote_address,
    default_limits= ["100 per day", "50 per hour"]
)
def limiter_routes(app: Flask):
    
    limiter.init_app(app)
    
    @app.errorhandler(429)
    def request_limit_error(e):
        #log add
        app.logger.info("limite de requisição excedido")
        return jsonify({"error": "limite de requisição exedido tente novamente mais tarde"}),429