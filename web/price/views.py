from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import View
from price.models import *
from utils import jwt_manager
import json

jwt_m = jwt_manager.JwtManager()


class LoginView(View) :
    def get(self, request):
        return render(request, "price/index.html")
        
    
    
class UrlListView(View):  # View를 상속받는다.
    
    def get(self, request):
        jwt_token = request.COOKIES.get("basic")
        decoded_jwt = jwt_m.validate_token(jwt_token)
        if decoded_jwt :
            
            user_id = jwt_m.get_user_id(decoded_jwt)
        #view logic
            user = User.objects.get(user_id = user_id)
            user_urls = UserUrl.objects.select_related('url').filter(user=user.user_id)
            links = []
            for user_url in user_urls :
                links.append(user_url.url.url_link)
        
            return render(request, "price/data.html", {"links" : links})
        else :
            return HttpResponseNotFound("NO!!!!!!!! TTTTTTTTTTTTTTT")
        return render(request, "price/index.html")
    
    

