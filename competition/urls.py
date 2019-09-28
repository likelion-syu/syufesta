from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('' , views.home, name="comp_home" ),
    path('event', views.event, name='event'),
    path('timeline', views.timeline , name='timeline'),
    path('notice', views.notice, name='notice'),
    path('seatmap', views.seatmap, name='seatmap'),
    path('foodtruck', views.foodtruck, name='compete_foodtruck'),
    path('foodtruck_detail', views.foodtruck_detail, name='compete_foodtruck_detail'),
    path('test', views.major_data, name = 'major_data'),
    path('data', views.data_test, name = "data_test")
]