from flask import request, jsonify


def register_routes(app):
    
    @app.route('/test', methods = ['GET'])
    def hello():
        return jsonify({"message": 'Hello, chill guy'})
    
    
    
    