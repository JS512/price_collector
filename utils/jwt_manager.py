import jwt, datetime
import http, json

SECRET_PRE = "personal_choose"
ALGORITHM = 'HS256'

class CookieManager() :
    
    def create_cookie(self, resp, value, name="basic") :
        resp.set_cookie(name, value = value, max_age = None, expires = None, path = '/', domain = None, 
                        secure = None, httponly = False)
class JwtManager() :
    
    def create_token(self, email):
        encoded = jwt.encode(
            payload = {'exp':datetime.datetime.utcnow() + datetime.timedelta(seconds = 300),
                    'email': email},
            key = SECRET_PRE, 
            algorithm = ALGORITHM)
        return encoded
    
    
    def validate_token(self, get_token):
        try:
            return jwt.decode(get_token, SECRET_PRE, algorithms = ALGORITHM, options={"verify_signature" : True})
        except Exception as e :
            print(e)
            return False
        except jwt.ExpiredSignatureError:
            return False
        except jwt.InvalidTokenError:
            return False
        
    def get_user_id(self, decoded_token) :
        
        return decoded_token["email"]