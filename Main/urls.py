from django.urls import path
from Main import views

urlpatterns = [
    path('', views.index, name = "index"),
]
