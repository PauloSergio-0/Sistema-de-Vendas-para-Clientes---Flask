import jwt
from jwt import PyJWKError
from settings.jwt_config import Config_Jwt

class Jwt_service:
    
    def decode_jwt(token):
        try:
            
            payload = jwt.decode(token, Config_Jwt.SECRET_KEY, algorithms = [Config_Jwt.ALGORITHM])
            
            print('payload')
            print(payload)
            return payload
        except PyJWKError:
            return None
        
        