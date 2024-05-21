from django.contrib import admin
from django.urls import path , include
from home import views

urlpatterns = [
    path("",views.sui),
    path("home/",views.home),
    path("dashboard/",views.dashboard),
]