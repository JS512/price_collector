from django.urls import path
from . import views

urlpatterns = [
    path("data/", views.UrlListView.as_view(),name='urllist'),
    path("login/", views.LoginView.as_view(),name='login'),
    path("data/user_price", views.DataView.as_view(),name='user_price'),
    path("save_url/", views.SaveDataView.as_view(),name='save_urls'),
    path("send_push/", views.send_push_notification, name="send_push"),
    path("save_subscription/", views.save_subscription, name="save_subscription"),
    path("test/", views.save_subscription2, name="save_subscription2"),
]