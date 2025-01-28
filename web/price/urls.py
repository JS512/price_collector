from django.urls import path

from . import views

urlpatterns = [
    path("", views.UrlListView.as_view(),name='urllist'),
]