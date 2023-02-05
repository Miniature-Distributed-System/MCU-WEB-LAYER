from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('login',views.login, name = "login"),
    path('signup',views.signup, name = "signup"),
    path('homepage',views.homepage,name = "homepage"),
    path('delete/<int:id>,<int:userid>,<str:file_name>,<str:instance_type>',views.delete,name="delete"),
    path('result/<str:loginuserid>,<str:file_name>,<str:instance_type>',views.result,name="result")
]
