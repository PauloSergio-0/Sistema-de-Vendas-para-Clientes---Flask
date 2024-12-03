from flask import jsonify, request, Flask
from service.venda_service import Service_venda
from decorators.jwt_required import jwt_required
from utils.json_validator import Validator

def register_venda_routes(app: Flask):
    
    @app.route("/cadastro/venda", methods=["POST"])
    @jwt_required
    def insert_venda():
        json_venda = request.get_json()
        print(json_venda)
        
        if Validator.venda_json(json_venda):
            Service_venda.insert_venda(json_venda)
            
        return jsonify({'message': "venda cadastrado"}), 201
    
    @app.route("/listar/venda", methods=['GET'])
    def listar_venda():
        return Service_venda.list_venda()
    
    @app.route("/filtro/venda", methods = ['GET'])
    def filtro_venda():
        id_venda = request.args.get("id_venda")
        return jsonify({"mensage": Service_venda.filter_vendas(id_venda)})
    
    @app.route("/filtro/venda-data", methods = ['GET'])
    def filtro_venda_data():
        data_venda: str = request.args.get("data_venda")
        return jsonify({"mensage": Service_venda.filter_date_vendas(data_venda)})
    