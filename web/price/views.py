from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.views.generic import View
from flask import jsonify
from price.models import *
from webpush.models import PushInformation
from utils import jwt_manager
from connector import db_connector
import json

jwt_m = jwt_manager.JwtManager()
db_conn = db_connector.DBConnector()

class LoginView(View) :
    def get(self, request):
        return render(request, "price/index.html")
        

class DataView(View) :
    def get(self, request) :
        rs = {
            "links" : [],
            "chart_data" : []
        }
        
        jwt_token = request.COOKIES.get("basic")
        decoded_jwt = jwt_m.validate_token(jwt_token)
        
        user_id = jwt_m.get_user_id(decoded_jwt)
        #view logic
        user = User.objects.get(user_id = user_id)
        user_urls = UserUrl.objects.select_related('url').filter(user=user.user_id)
        
        for user_url in user_urls :
            rs["links"].append(user_url.url.url_link)
            rs_price_data = {
                "data" : [],
                "labels" : []
            }
            price_data = PriceData.objects.filter(url_id=user_url.url.id)
            
            for price in price_data.iterator() :
                rs_price_data["data"].append(price.discount_price)
                rs_price_data["labels"].append(price.collect_ts)
            rs["chart_data"].append(rs_price_data)
        
        return JsonResponse(rs)
    
class UrlListView(View):  # View를 상속받는다.
    
    def get(self, request):
        
        jwt_token = request.COOKIES.get("basic")
        decoded_jwt = jwt_m.validate_token(jwt_token)
        if decoded_jwt :
            return render(request, "price/data.html")
        else :
            return render(request, "price/index.html")
        return render(request, "price/index.html")
    
    
    
    

class SaveDataView(View) :
    def post(self, request) :
        jwt_rs = jwt_m.validate_token(request.COOKIES.get("basic"))
        if jwt_rs :
            urls = json.loads(request.body)['urls']
            save_data = [(url,) for url in urls]
            db_conn.save_url_data(jwt_m.get_user_id(jwt_rs), save_data)
        # else :

import json
from django.http import JsonResponse
from webpush import send_user_notification
from django.contrib.auth.models import User


def send_push_notification(request):
    user = User.objects.get(email="shdzl@naver.com")
    from webpush import send_user_notification

    payload = {"head": "Welcome!", "body": "Hello World"}

    send_user_notification(user=user, payload=payload, ttl=1000)
    
    
import json
from django.http import JsonResponse


def save_subscription(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_id = data.get('user_id')
        user = User.objects.get(email='shdzl@naver.com')
        # user = User.objects.create_user(username='222',
        #                          email='shdzl@naver.com',
        #                          password='glass onion')
        # 유저의 Web Push 정보 저장
        # push_info, created = PushInformation.objects.get_or_create(user=user)
        # push_info.subscription = data
        # push_info.save()

        return JsonResponse({"message": "Subscription saved!"}, status=201)

    return JsonResponse({"error": "Invalid request"}, status=400)



def save_subscription2(request) :
    return render(request, "price/test.html")