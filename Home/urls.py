from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('login',views.login, name = "login"),
    path('signup',views.signup, name = "signup"),
    path('homepage',views.homepage,name = "homepage"),
    path('devlogin',views.devlogin,name = "devlogin"),
    path('devhome',views.devhome,name = "devhome"),
    path('clientlog/<str:devid>',views.clientlog,name = "clientlog"),
    path('viewactiveinstance/<str:devid>',views.viewactiveinstance,name="viewactiveinstance"),
    path('delete/<int:id>,<int:userid>,<str:file_name>,<str:instance_type>',views.delete,name="delete"),
    path('result/<str:loginuserid>,<str:file_name>,<str:instance_type>',views.result,name="result"),
    path('deleteInstance/<str:active_instance_id>',views.deleteInstance,name="deleteInstance")
]
