from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('booth', views.BoothViewSet)

urlpatterns = [
    path('event', views.event, name='event'),
    path('timeline', views.timeline , name='timeline'),
    path('notice', views.notice, name='notice'),
    path('seatmap', views.seatmap, name='seatmap'),
    path('foodtruck', views.foodtruck, name='compete_foodtruck'),
    path('restframework/', include(router.urls)),
]