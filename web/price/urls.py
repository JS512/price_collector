from django.urls import path

from . import views

urlpatterns = [
    path("data/", views.UrlListView.as_view(),name='urllist'),
    path("login/", views.LoginView.as_view(),name='login'),
]