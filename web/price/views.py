from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.views.generic import View
from flask import jsonify
from price.models import *
from utils import jwt_manager
import json

jwt_m = jwt_manager.JwtManager()


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
    
    
    
    

