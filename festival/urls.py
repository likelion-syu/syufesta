from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('foodtruck', views.foodtruck, name='fest_foodtruck'),
	path('booth', views.booth, name='booth'),
	path('stamp', views.stamp, name='stamp'),
	path('contest/talent', views.talent, name='talent'),
	path('contest/cheer', views.cheer, name='cheer'),
]