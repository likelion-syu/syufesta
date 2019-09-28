from django.shortcuts import render, get_object_or_404
from django.db import connection
from django.http import JsonResponse
from .models import Major, Foodtruck, FoodtruckMenu, Booth
from . import utils

# from models import Booth , FoodTruck
# Create your views here.
def home(request):
    return render (request, 'common/index.html')

def comp_booth(req , pk):
    with connection.cursor() as cursor:
        cursor.execute("select * from Booth where booth_id = " + str(pk))
        rows = cursor.fetchall()
    
    expanded_rows = []
    expanded_rows = utils.query_expand(rows, cursor)
    
    return render(req , 'common/popup/competition/foodtruck.html' , {
        'data' : expanded_rows[0]
    })

def comp_foodtruck(req , pk):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM FoodTruck WHERE truck_id = " + str(pk))
        rows = cursor.fetchall()
    
    expanded_rows = []
    expanded_rows = utils.query_expand(rows , cursor)

    return render(req , 'common/popup/competition/foodtruck.html' , {
        'data' : expanded_rows[0]
    })



def comp_seatmap(req , pk):
    major_detail = get_object_or_404(Major, pk=pk)

    return render(req , 'common/popup/competition/seatmap.html', {'major': major_detail})

def fest_foodtruck(req, pk):
    foodtruck_detail = get_object_or_404 (Foodtruck, pk=pk)
    foodtruck_menu = FoodtruckMenu.objects.filter(truck = pk)
    return render(req, 'common/popup/festival/foodtruck.html', {'food': foodtruck_detail, 'menus':foodtruck_menu})

def fest_booth(req, pk):
    booth_detail = get_object_or_404(Booth, pk=pk)
    return render(req, 'common/popup/festival/booth.html', {'booth': booth_detail})

