from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
	path('', views.main, name='fest_home'),
	path('foodtruck', views.foodtruck, name='fest_foodtruck'),
	path('festmap', views.festmap, name='festmap'),
	path('stamp', views.stamp, name='stamp'),
	path('contest/talent', views.talent, name='talent'),
	path('contest/cheer', views.cheer, name='cheer'),
	path('foodtruck1',views.popup1, name='foodtruck1'),
	path('contest/talent_select', views.talent_select, name = 'talent_select'),
	path('signin/' , views.signin , name="signin"),
	path('signup/' , views.signup , name="signup"),
	path('signout/' , views.signout , name="signout"),
]