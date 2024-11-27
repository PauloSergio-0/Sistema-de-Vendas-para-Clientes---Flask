from .authorization_routes import register_routes_authorization
from .cliente_routes import register_clientes_routes
from .test_routes import register_routes

def routes_flask(app):
    
    register_clientes_routes(app)
    register_routes_authorization(app)
    register_routes(app)