from django.shortcuts import render, get_object_or_404
from django.db import connection
from django.http import JsonResponse
from .models import Major, Foodtruck, FoodtruckMenu
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
    foodtruck_detail = get_object_or_404(Foodtruck, pk=pk)

    return render(req , 'common/popup/competition/foodtruck.html' , {
        'data' : foodtruck_detail
    })



def comp_seatmap(req , pk):
    with connection.cursor() as cursor:
        cursor.execute("select * ,MJ_A.major_name as 'major_a_name' ,MJ_A.major_logo_url as 'major_a_logo_url' ,MJ_B.major_name as 'major_b_name' ,MJ_B.major_logo_url as 'major_b_logo_url'from MatchSchedule as MS join Major as MJ_A join Major as MJ_B on MS.sch_major_a = MJ_A.major_id and MS.sch_major_b = MJ_B.major_id WHERE truck_id = " + str(pk))
        rows = cursor.fetchall()
    
    expanded_rows = []
    expanded_rows = utils.query_expand(rows , cursor)

    return render(req , 'common/popup/competition/foodtruck.html' , {
        'data' : expanded_rows[0]
    })

    # major_detail = get_object_or_404(Major, pk=pk)

    # return render(req , 'common/popup/competition/seatmap.html', {'major': major_detail})


