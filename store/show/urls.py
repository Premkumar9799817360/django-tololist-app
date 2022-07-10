from django.contrib import admin
from django.urls import path , include
from show import views

urlpatterns = [
    path('', views.index, name="index"),
    path('chack', views.chack, name="chack")

]