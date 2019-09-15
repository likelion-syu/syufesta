from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('event/', views.compete_event, name='event'),
    path('timeline/', views.compete_timeline , name='compete_timeline'),
    path('safety/', views.safety, name='safety'),
    path('seatmap/', views.seat_map, name='seat_map'),
    path('foodtruck', views.food_truck, name='compete_food_truck')
]