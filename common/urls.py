from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('popup/comp/foodtruck/<int:pk>' , views.comp_foodtruck , name="popup_comp_foodtruck"),
    path('fest/talent', views.fest_talent, name = "fest_talent")
]