import jwt
from jwt import PyJWKError
from settings.jwt_config import Config_Jwt

class Jwt_service:
    
    def decode_jwt(token):
        try:
            
            payload = jwt.decode(token, Config_Jwt.SECRET_KEY, algorithms = [Config_Jwt.ALGORITHM])
            return payload
        
        except PyJWKError:
            return None
        
        