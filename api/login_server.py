from flask import Flask, request, make_response
from flask.views import View, MethodView
from connector import db_connector, redis_connector
from flask_cors import CORS, cross_origin
from flask import Response
import json,jwt, datetime
import http


app = Flask(__name__)

db = db_connector.DBConnector()
CORS(app, origins=["*"], supports_credentials=True)



SECRET_PRE = "personal_choose"

class CookieManager() :
    
    def create_cookie(self, resp, value, name="basic") :
        resp.set_cookie(name, value = value, max_age = None, expires = None, path = '/', domain = None, 
                        secure = None, httponly = False)
class JwtManager() :
    def __init__(self):
        self.algorithm = 'HS256'
        
    
    def create_token(self, email):
        encoded = jwt.encode(
            payload = {'exp':datetime.datetime.utcnow() + datetime.timedelta(seconds = 300),
                    'email': email},
            key = SECRET_PRE, 
            algorithm = self.algorithm)
        return encoded
    
    
    def validate_token(self, get_token):
        try:
            print(jwt.decode(get_token, SECRET_PRE, algorithms = self.algorithm, options={"verify_signature" : True}))
        except Exception as e :
            print(e)
        except jwt.ExpiredSignatureError:
            return http.HTTPStatus.UNAUTHORIZED
        except jwt.InvalidTokenError:
            return http.HTTPStatus.UNAUTHORIZED
        else:
            return True
        
        
jwt_m = JwtManager()
cookie_m = CookieManager()

class LoginProcessor(MethodView) :
    def __init__(self):
        pass
    
    
    def post(self):
    
        params = request.get_json()
        user_data = db.get_user_data_with_pw(params["id"], params["pw"]) 
        
        
        response = make_response()
        response.mimetype = "application/json"
        
        
        # if True :
        if user_data :
            print(params["id"], type(params["id"]))
            token = jwt_m.create_token(params["id"])
            # cookie_m.create_cookie(response, token)
            response.set_cookie("basic", value = token, max_age = None, expires = None, path = '/', domain = None, 
                        secure = None, httponly = True)            
            response.data = json.dumps({"message" : "로그인 성공"})
            response.status_code = 200
        else :   
            response.data = json.dumps({"message" : "로그인 실패"})
            response.status_code = 401
        
        return response
    
    def get(self) :
        print('test')
        data = request.cookies.get("basic")
        print(jwt_m.validate_token(data))
        return "text"
    def check_login(self) :
        pass



    
# @app.route("/login", methods=["POST"])
# def dispatch_request():
#     if request.method == "POST":
#         params = request.get_json()
#         user_data = db.get_user_data_with_pw(params["id"], params["pw"]) 
#         if user_data :
#             return "Success", 200
#         else :
#             return "Authorized Error", 401
@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/22')
def home2() :
    return "test";

if __name__ == '__main__':
    app.add_url_rule("/login", view_func=LoginProcessor.as_view("login"), methods=["GET", "POST"])
    app.run(debug=True, port=5055)