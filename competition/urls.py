from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.com_home, name='com_home'),
    path('<int:major_id>', views.com_tl_detail, name='com_tl_detail'),
    path('compete_timeline/', views.com_tl , name='com_tl')
]