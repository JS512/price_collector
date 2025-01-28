from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from price.models import *

class UrlListView(View):  # View를 상속받는다.
    
    def get(self, request):
        user_id = "shdzl@naver.com"
        #view logic
        user = User.objects.get(user_id = user_id)
        user_urls = UserUrl.objects.select_related('url').filter(user=user.user_id)
        links = []
        for user_url in user_urls :
            links.append(user_url.url.url_link)
        
        return render(request, "price/index.html", {"links" : links})
