from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('login',views.login, name = "login"),
    path('homepage',views.homepage,name = "homepage")
]
