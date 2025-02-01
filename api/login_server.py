from flask import Flask, request, make_response
from flask.views import View, MethodView
from connector import db_connector, redis_connector
from flask_cors import CORS, cross_origin
from flask import Response
import json
from utils import jwt_manager


app = Flask(__name__)

db = db_connector.DBConnector()
CORS(app, origins=["*"], supports_credentials=True)

jwt_m = jwt_manager.JwtManager()
cookie_m = jwt_manager.CookieManager()

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

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/22')
def home2() :
    return "test";

if __name__ == '__main__':
    app.add_url_rule("/login", view_func=LoginProcessor.as_view("login"), methods=["GET", "POST"])
    app.run(debug=True, port=5055)