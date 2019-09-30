from django.contrib import admin
from django.urls import path, include
from . import views

# localhost:8000/common/popup/comp/seatmap/1
urlpatterns = [
    path('popup/comp/foodtruck/<int:pk>' , views.comp_foodtruck , name="popup_comp_foodtruck"),
    path('popup/comp/booth/<int:pk>' , views.comp_foodtruck , name="popup_comp_booth"),
    path('popup/comp/seatmap/<int:pk>' , views.comp_seatmap , name="popup_comp_seatmap"),
    path('fest/contest/result', views.talent_result, name="result"),
    path('popup/fest/foodtruck/<int:pk>', views.fest_foodtruck, name = "popup_fest_foodtruck"),
    path('popup/fest/booth/<int:pk>', views.fest_booth , name = "popup_fest_booth"),
    path('popup/fest/festmap_popup1', views.festmap_popup1, name = "festmap_popup1"),
    path('popup/fest/festmap_popup2', views.festmap_popup2, name = "festmap_popup2"),

    # API
    path('fest/contest/vote' , views.contest_vote , name="contest_vote"),
    path('fest/contest/revote' , views.contest_revote , name="contest_revote"),
]
