from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('login',views.login, name = "login"),
    path('signup',views.signup, name = "signup"),
    path('homepage',views.homepage,name = "homepage"),
    path('delete/<int:id>',views.delete,name="delete")
]
