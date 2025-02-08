from django.urls import path

from . import views

urlpatterns = [
    path("data/", views.UrlListView.as_view(),name='urllist'),
    path("login/", views.LoginView.as_view(),name='login'),
    path("data/user_price", views.DataView.as_view(),name='user_price'),
    path("save_url/", views.SaveDataView.as_view(),name='save_urls'),
]